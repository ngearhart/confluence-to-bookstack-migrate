
from dataclasses import dataclass
from typing import List

from requests import get

from data.agnostic import Category
from data.confluence.space import SpaceQuery


@dataclass
class ConfluenceLoader:

    url: str
    access_token: str

    def format_url(self, path):
        return f'https://{self.url}/{path}'

    def request_kwargs(self):
        return {
            'headers': {
                'Authorization': f'Bearer {self.access_token}'
            }
        }

    def perform_space_query(self) -> SpaceQuery:
        return SpaceQuery.from_dict(
            get(
                self.format_url('rest/api/space'),
                **self.request_kwargs()
            ).json()
        )

    def load() -> List[Category]:
        pass
