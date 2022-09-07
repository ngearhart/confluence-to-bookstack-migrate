from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    name: str
    tags: List[str]
    id: int | None
    description: str | None
    image: str | None


@dataclass
class Chapter:
    name: str
    book_id: int
    tags: List[str]
    id: int | None
    description: str | None


@dataclass
class Page:
    name: str
    book_id: int
    markdown: str  # TODO: Support html
    tags: List[str]
    id: int | None
    chapter_id: int | None
