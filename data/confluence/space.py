from dataclasses import dataclass
from typing import List

from dataclass_wizard import JSONWizard

from data.agnostic import Category


@dataclass
class SpaceQuery(JSONWizard):
    """Dataclass for the response from Confluence when querying spaces."""
    results: List['Space']
    start: int
    limit: int
    size: int
    _links: '_links'

    def to_agnostic(self) -> List[Category]:
        return [
            Category(
                slug=space.key,
                name=space.name,
                confluence_id=space.id
            ) for space in self.results
        ]


@dataclass
class Space:
    """Dataclass representing basic information about a confluence space."""
    id: int
    key: str
    name: str
    type: str
    _links: '_links'
    _expandable: '_expandable'


@dataclass
class _links:
    """
    _links dataclass

    """
    webui: str
    self: str


@dataclass
class _expandable:
    """
    _expandable dataclass

    """
    metadata: str
    icon: str
    description: str
    homepage: str


@dataclass
class _links:
    """
    _links dataclass

    """
    self: str
    base: str
    context: str
