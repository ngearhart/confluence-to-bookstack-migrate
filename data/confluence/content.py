from dataclasses import dataclass
from typing import List, Union
from data import agnostic

from dataclass_wizard import JSONWizard


@dataclass
class ContentQuery(JSONWizard):
    """Dataclass representing the content from a Confluence space."""
    page: 'ContentResult'
    blogpost: 'Blogpost'
    _links: '_links'

    def to_agnostic(self) -> List[agnostic.Page]:
        return [
            page.to_agnostic() for page in self.page.results
        ]


@dataclass
class ContentResult:
    """
    Page dataclass

    """
    results: List['Page']
    start: int
    limit: int
    size: int
    _links: '_links'


@dataclass
class Page(JSONWizard):
    """
    Result dataclass

    """
    id: Union[int, str]
    type: str
    status: str
    title: str
    _links: '_links'
    _expandable: '_expandable'
    extensions: 'Extensions' = None

    def to_agnostic(self) -> agnostic.Page:
        return agnostic.Page(
            confluence_id=self.id,
            name=self.title,
            children=[]
        )


@dataclass
class Extensions:
    """
    Extensions dataclass

    """
    position: Union[str, int]


@dataclass
class _expandable:
    """
    _expandable dataclass

    """
    container: str
    metadata: str
    operations: str
    children: str
    history: str
    ancestors: str
    body: str
    version: str
    descendants: str
    space: str
    restrictions: str = None


@dataclass
class _links:
    """
    _links dataclass

    """
    self: str = None
    base: str = None
    context: str = None
    webui: str = None
    edit: str = None
    tinyui: str = None


@dataclass
class Blogpost:
    """
    Blogpost dataclass

    """
    results: List
    start: int
    limit: int
    size: int
    _links: '_links'
