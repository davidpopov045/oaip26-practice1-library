from Book import Book
from User import Reader, Librarian, User
import sys
from dataclasses import dataclass
from MenuState import MenuState


def main():
    state = MenuState()

    generate_test_data()

    load_data(state)    
    login(state)
    state.current_user.menu(state)
    save_data(state)
    print("Данные сохранены. До свидания!")
    sys.exit(0)        

def load_data(state):    
    state.books = Book.load_books("books.txt")
    state.users = User.load_users("users.txt")

def save_data(state):
    Book.save_books("books.txt", state.books)
    User.save_users("users.txt", state.users)


def login(state):    
    print("Добро пожаловать в библиотеку!")

    if not state.users:
        print(f"Первый запуск. Регистрация как первый библиотекарь.")
        name = input("Введите ваше имя: ")
        new_id = 1
        new_user = Librarian(new_id, "librarian", name)
        state.users.append(new_user)
        current_user = new_user
        print(f"Библиотекарь {name} зарегистрирован и вошел в систему!")
    else:
        name = input("Введите ваше имя: ")        
        user = User.find_user_by_name(name, state.users)        
        if not user:                    
            print(f"Пользователь {name} не найден!")
            sys.exit(1)        
        state.current_user = user
        print(f"Добро пожаловать, {name}!")


def generate_test_data():
    books = [
        Book(1, "Мастер и Маргарита", "Михаил Булгаков", "available"),
        Book(2, "Война и мир", "Лев Толстой", "taken"),
        Book(3, "Сон в красном тереме", "Цао Сюэцинь", "available"),
        Book(4, "Путешествие на Запад", "У Чэнъэнь", "taken"),
        Book(5, "Одиссея", "Гомер", "available"),
        Book(6, "Илиада", "Гомер", "taken"),
        Book(7, "Мхитар Спарапет", "Мурацан", "available"),
        Book(8, "Давид Сасунский", "Ованес Туманян", "taken"),
        Book(9, "Тысяча и одна ночь", "Неизвестный", "available"),
        Book(10, "Калила и Димна", "Ибн аль-Мукаффа", "taken")
    ]
    
    users = []
    
    readers = [
        Reader(1, "reader", "Андрей Петров", [2]),
        Reader(2, "reader", "Иван Иванов", [4, 6]),
        Reader(3, "reader", "Чжан Вэй", [8]),
        Reader(4, "reader", "Ли На", [10]),
        Reader(5, "reader", "Георгиос Пападопулос", []),
        Reader(6, "reader", "Мария Константину", []),
        Reader(7, "reader", "Айк Ованисян", []),
        Reader(8, "reader", "Анаит Саркисян", []),
        Reader(9, "reader", "Мухаммад Ахмед", []),
        Reader(10, "reader", "Фатима Али", [])
    ]
    
    librarians = [
        Librarian(101, "librarian", "Светлана Сидорова"),
        Librarian(102, "librarian", "Ван Мин")
    ]
    
    users.extend(readers)
    users.extend(librarians)
    
    Book.save_books("books.txt", books)
    User.save_users("users.txt", users)    
    

main()