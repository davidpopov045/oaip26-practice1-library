from Book import Book
from User import Reader, Librarian

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

def save_users(filename, users):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"{len(users)}\n")
        for user in users:
            f.write(f"{user.id}\n")
            f.write(f"{user.type}\n")
            f.write(f"{user.name}\n")
            if user.type == "reader":
                f.write(" ".join(str(bid) for bid in user.books_taken) + "\n")

def load_users(filename):
    users = []
    with open(filename, 'r', encoding='utf-8') as f:
        count = int(f.readline().strip())
        for _ in range(count):
            user_id = int(f.readline().strip())
            user_type = f.readline().strip()
            name = f.readline().strip()
            if user_type == "reader":
                books_line = f.readline().strip()
                books_taken = [int(bid) for bid in books_line.split()] if books_line else []
                users.append(Reader(user_id, user_type, name, books_taken))
            elif user_type == "librarian":
                users.append(Librarian(user_id, user_type, name))
    return users