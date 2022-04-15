
from dataclasses import dataclass
from typing import List

from data.agnostic import Category


@dataclass
class ConfluenceLoader:

    access_token: str

    def load() -> List[Category]:
        pass
