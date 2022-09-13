
from dataclasses import dataclass, replace
from typing import List, Union
from functools import cached_property


def slugify(name: str):
    return name.lower().strip().replace(' ', '-')


@dataclass
class Page:
    name: str
    html: str = None
    confluence_id: str = None
    bookstack_id: int = None
    children: List['Page'] = None

    def to_hierarchy(self, level: int = 0) -> str:
        tab_prefix = ''.join('\t' * level)
        if self.children is not None and len(self.children) > 0:
            children_print = '\n'.join([
                child.to_hierarchy(level + 1) for child in self.children
            ])
            return f"{tab_prefix}- {self.name}\n{children_print}"
        return f"{tab_prefix}- {self.name}"

    def add_child(self, child: 'Page'):
        self.children.append(child)

    @cached_property
    def max_child_depth(self):
        if self.children is None or len(self.children) == 0:
            return 0  # I am a leaf
        return max(child.max_child_depth for child in self.children) + 1

    def flatten(self, parent: Union['Page', 'Category'], current_depth, tag_depth, max_depth):
        # If this page has no children, immediately throw it on the parent
        if self.children is None or len(self.children) == 0:
            parent.add_child(replace(self))
            return
        # Also, if we have exceeded max depth
        if current_depth >= max_depth:
            parent.add_child(replace(self))
            for child in self.children:
                # Simply force all these children onto the same parent
                child.flatten(parent, current_depth, tag_depth, max_depth)
            return
        # We have at least 1 child and 1 depth left
        # Do we have more than max depth children?
        # if self.max_child_depth > max_depth - current_depth:

        # Write a new chapter and introduction
        new_category = Category(slugify(self.name), self.name)
        new_category.pages = [
            Page('Introduction', confluence_id=self.confluence_id),
        ]
        for child in self.children:
            child.flatten(new_category, current_depth + 1, tag_depth, max_depth)
        parent.pages.append(new_category)

        # else:  # No? Then just append to the category
        #     parent.add_child(replace(self))
        #     for child in self.children:
        #         # Simply force all these children onto the same parent
        #         child.flatten(parent, current_depth, tag_depth, max_depth)


@dataclass
class Category:
    slug: str
    name: str
    pages: List[Page] = None
    confluence_id: int = None
    bookstack_id: int = None

    def to_hierarchy(self, depth: int = 1) -> str:
        pages = '\n'.join(page.to_hierarchy(depth) for page in self.pages)
        return f'{self.name}\n{pages}'

    def add_child(self, child: 'Page'):
        self.pages.append(child)

    def flatten(self, tag_depth: int=2, max_depth: int=3):
        """
        @param tag_depth The depth above a child at which to start assigning tags.
        @param max_depth The max depth to preserve.
        """
        outcome = replace(self)
        outcome.pages = []
        for page in self.pages:
            page.flatten(outcome, 0, tag_depth, max_depth)
        return outcome
