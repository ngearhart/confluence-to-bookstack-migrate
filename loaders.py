
from dataclasses import dataclass
from typing import List

from requests import get

from data.agnostic import Category
from data import agnostic
from data.confluence.content import Page
from data.confluence.space import Space, SpaceQuery


def paginated(func):
    def wrapper(*args, **kwargs):
        response, headers, base_url = func(*args, **kwargs)
        if response.status_code == 200:
            data = response.json()
            yield from data['results']
            while 'next' in data['_links']:
                response = get(base_url + data['_links']['next'], headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    yield from data['results']
    return wrapper


@dataclass
class ConfluenceLoader:
    """
    Thanks to https://stackoverflow.com/a/70089434
    """

    url: str
    access_token: str

    @property
    def base_url(self):
        return f'https://{self.url}'

    def headers(self):
        return {
            'Authorization': f'Bearer {self.access_token}'
        }

    @paginated
    def perform_space_query(self) -> list:
        return get(
            self.base_url + '/rest/api/space',
            headers=self.headers()
        ), self.headers(), self.base_url

    @paginated
    def perform_root_content_query(self, spaceKey) -> list:
        return get(
            self.base_url + f'/rest/api/space/{spaceKey}/content/page?depth=root',
            headers=self.headers()
        ), self.headers(), self.base_url

    @paginated
    def get_page_children(self, parentId) -> list:
        return get(
            self.base_url + f'/rest/api/content/search?cql=parent={parentId}',
            headers=self.headers()
        ), self.headers(), self.base_url

    def populate_page_children(self, page: agnostic.Page):
        for child in self.get_page_children(page.confluence_id):
            agnostic_child = Page.from_dict(child).to_agnostic()
            page.children.append(agnostic_child)
            self.populate_page_children(agnostic_child)

    def load(self) -> List[Category]:
        confluence_spaces = Space.from_list(self.perform_space_query())
        agnostic_categories = []
        for space in confluence_spaces[:10]:
            agnostic_category = space.to_agnostic()
            root_content = Page.from_list(self.perform_root_content_query(space.key))
            for root_page in root_content:
                agnostic_page = root_page.to_agnostic()
                agnostic_category.pages.append(agnostic_page)
                self.populate_page_children(agnostic_page)
            agnostic_categories.append(agnostic_category)
            print(agnostic_category.to_hierarchy())
        
