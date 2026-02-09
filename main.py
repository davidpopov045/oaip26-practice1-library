from Book import Book
from User import Reader, Librarian
import Database

def main():
    generate_test_data()
    pass


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
    
    Database.save_books("books.txt", books)
    Database.save_users("users.txt", users)    
    

main()