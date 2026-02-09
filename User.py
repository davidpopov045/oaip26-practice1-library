from dataclasses import dataclass
from typing import List

@dataclass
class User:
    id: int
    type: str
    name: str


@dataclass
class Reader(User):
    books_taken: List[int] = None
    
    def __post_init__(self):
        if self.books_taken is None:
            self.books_taken = []

@dataclass
class Librarian(User):
    pass