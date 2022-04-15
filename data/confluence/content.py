from dataclasses import dataclass
from typing import List, Union
import agnostic

from dataclass_wizard import JSONWizard


@dataclass
class ContentQuery(JSONWizard):
    """Dataclass representing the content from a Confluence space."""
    page: 'ContentResult'
    blogpost: 'Blogpost'
    _links: '_links'

    def to_agnostic(self) -> List[agnostic.Page]:
        return [
            agnostic.Page(
                confluence_id=page.id,
                name=page.title
            ) for page in self.page.results
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
class Page:
    """
    Result dataclass

    """
    id: Union[int, str]
    type: str
    status: str
    title: str
    extensions: 'Extensions'
    _links: '_links'
    _expandable: '_expandable'


@dataclass
class Extensions:
    """
    Extensions dataclass

    """
    position: Union[str, int]


@dataclass
class _links:
    """
    _links dataclass

    """
    webui: str
    edit: str
    tinyui: str
    self: str


@dataclass
class _expandable:
    """
    _expandable dataclass

    """
    container: str
    metadata: str
    operations: str
    children: str
    restrictions: str
    history: str
    ancestors: str
    body: str
    version: str
    descendants: str
    space: str


@dataclass
class _links:
    """
    _links dataclass

    """
    self: str


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


@dataclass
class _links:
    """
    _links dataclass

    """
    self: str


@dataclass
class _links:
    """
    _links dataclass

    """
    base: str
    context: str
