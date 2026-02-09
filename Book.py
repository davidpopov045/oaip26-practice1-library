from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    id: int
    title: str
    author: str
    status: str = "available"