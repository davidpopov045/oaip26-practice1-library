from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from Book import Book

@dataclass
class User(ABC):
    id: int
    type: str
    name: str

    @abstractmethod
    def menu(self, state):
        pass
    
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
    
    def find_user_by_name(name, users):
        for user in users:
            if user.name == name:
                return user
        return None

@dataclass
class Reader(User):
    books_taken: List[int] = None
    
    def __post_init__(self):
        if self.books_taken is None:
            self.books_taken = []

    def menu(self, state):
        while True:
            print("\nМеню пользователя:")
            print("1) Доступные книги")
            print("2) Взять книгу")
            print("3) Вернуть книгу")
            print("4) Мои книги")
            print("5) Выход")
            
            choice = input("Выбор: ")
            
            if choice == "1":
                for book in state.books:
                    if book.status == "available":
                        print(f"{book.id}: {book.title} ({book.author})")
            
            elif choice == "2":
                for book in state.books:
                    if book.status == "available":
                        print(f"{book.id}: {book.title}")
                
                try:
                    book_id = int(input("ID книги: "))
                    for book in state.books:
                        if book.id == book_id and book.status == "available":
                            book.status = "taken"
                            self.books_taken.append(book_id)
                            print(f"Книга '{book.title}' взята!")
                            break
                except:
                    print("Ошибка!")
            
            elif choice == "3":
                if not self.books_taken:
                    print("У вас нет книг!")
                    continue
                
                for book_id in self.books_taken:
                    for book in state.books:
                        if book.id == book_id:
                            print(f"{book.id}: {book.title}")
                
                try:
                    book_id = int(input("ID книги для возврата: "))
                    if book_id in self.books_taken:
                        self.books_taken.remove(book_id)
                        for book in state.books:
                            if book.id == book_id:
                                book.status = "available"
                                print(f"Книга '{book.title}' возвращена!")
                                break
                except:
                    print("Ошибка!")
            
            elif choice == "4":
                if not self.books_taken:
                    print("У вас нет книг!")
                    continue
                
                for book_id in self.books_taken:
                    for book in state.books:
                        if book.id == book_id:
                            print(f"{book.id}: {book.title} ({book.author})")
            
            elif choice == "5":
                break

@dataclass
class Librarian(User):
    
    def show_books_brief(books):
        for book in books:
            print(f"{book.id}: {book.title} ({book.status})")

    def show_users_brief(users):
        for user in users:
            print(f"{user.id}: {user.name} ({user.type})")

    def menu(self, state):
        while True:
            print("Меню библиотекаря:")
            print("1) Добавить книгу")
            print("2) Удалить книгу")
            print("3) Зарегистрировать пользователя")
            print("4) Список пользователей")
            print("5) Список всех книг")
            print("6) Выход")
            
            choice = input("Выбор: ")
            
            if choice == "1":
                new_id = max([b.id for b in state.books], default=0) + 1
                title = input("Название: ")
                author = input("Автор: ")
                
                print(f"\nID: {new_id}")
                print(f"Название: {title}")
                print(f"Автор: {author}")
                print(f"Статус: available")
                
                confirm = input("Подтвердить (y/n): ")
                if confirm.lower() == 'y':
                    state.books.append(Book(new_id, title, author, "available"))
                    print("Книга добавлена!")
            
            elif choice == "2":
                Librarian.show_books_brief(state.books)
                try:
                    book_id = int(input("ID книги для удаления: "))
                    for i, book in enumerate(state.books):
                        if book.id == book_id:
                            if book.status != 'available':
                                print('Книга не свободна. Нельзя удалить')
                                break
                            confirm = input(f"Удалить '{book.title}'? (y/n): ")
                            if confirm.lower() == 'y':
                                del state.books[i]
                                print("Книга удалена!")
                            break
                except:
                    print("Ошибка!")
            
            elif choice == "3":
                name = input("Имя нового пользователя: ")
                if User.find_user_by_name(name, state.users):
                    print("Пользователь уже существует!")
                    continue
                
                print("Тип пользователя:")
                print("1) Читатель")
                print("2) Библиотекарь")
                
                type_choice = input("Выбор: ")
                
                new_id = max([u.id for u in state.users], default=0) + 1
                
                if type_choice == "1":
                    new_user = Reader(new_id, "reader", name, [])
                elif type_choice == "2":
                    new_user = Librarian(new_id, "librarian", name)
                else:
                    print("Некорректный выбор!")
                    continue
                
                state.users.append(new_user)
                print(f"Пользователь {name} ({new_user.type}) зарегистрирован!")
            elif choice == "4":
                Librarian.show_users_brief(state.users)
            
            elif choice == "5":
                Librarian.show_books_brief(state.books)
            
            elif choice == "6":
                break








