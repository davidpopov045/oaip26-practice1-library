from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    id: int
    title: str
    author: str
    status: str = "available"

    def save_books(filename, books):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"{len(books)}\n")
            for book in books:
                f.write(f"{book.id}\n")
                f.write(f"{book.title}\n")
                f.write(f"{book.author}\n")
                f.write(f"{book.status}\n")

    def load_books(filename):
        books = []
        with open(filename, 'r', encoding='utf-8') as f:
            count = int(f.readline().strip())
            for _ in range(count):
                book_id = int(f.readline().strip())
                title = f.readline().strip()
                author = f.readline().strip()
                status = f.readline().strip()
                books.append(Book(book_id, title, author, status))
        return books