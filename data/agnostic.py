
from dataclasses import dataclass
from typing import List


@dataclass
class Page:
    name: str
    html: str = None
    confluence_id: str = None
    bookstack_id: int = None

@dataclass
class Category:
    slug: str
    name: str
    pages: List[Page] = None
    confluence_id: int = None
    bookstack_id: int = None
