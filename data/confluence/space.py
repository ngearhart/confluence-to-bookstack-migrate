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
            space.to_agnostic() for space in self.results
        ]


@dataclass
class Space(JSONWizard):
    """Dataclass representing basic information about a confluence space."""
    id: int
    key: str
    name: str
    type: str
    _links: '_links'
    _expandable: '_expandable'

    def to_agnostic(self) -> Category:
        return Category(
            slug=self.key,
            name=self.name,
            confluence_id=self.id,
            pages=[]
        )


@dataclass
class _links:
    """
    _links dataclass

    """
    webui: str = None
    self: str = None
    base: str = None
    context: str = None


@dataclass
class _expandable:
    """
    _expandable dataclass

    """
    metadata: str
    icon: str
    description: str
    homepage: str = None
