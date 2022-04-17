
from dataclasses import dataclass
from typing import List


@dataclass
class Page:
    name: str
    html: str = None
    confluence_id: str = None
    bookstack_id: int = None
    children: List['Page'] = None

    def to_hierarchy(self, level: int = 0) -> str:
        tab_prefix = ''.join('\t' * level)
        if len(self.children) > 0:
            children_print = '\n'.join([
                child.to_hierarchy(level + 1) for child in self.children
            ])
            return f"{tab_prefix}- {self.name}\n{children_print}"
        return f"{tab_prefix}- {self.name}"


@dataclass
class Category:
    slug: str
    name: str
    pages: List[Page] = None
    confluence_id: int = None
    bookstack_id: int = None

    def to_hierarchy(self) -> str:
        pages = '\n'.join(page.to_hierarchy(1) for page in self.pages)
        return f'{self.name}\n{pages}'
