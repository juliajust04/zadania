from zad_1 import Student


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka: {self.city}, {self.street}, "
            f"{self.zip_code}, godziny: {self.open_hours}, "
            f"telefon: {self.phone}"
        )


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik: {self.first_name} {self.last_name}, "
            f"data zatrudnienia: {self.hire_date}, "
            f"data urodzenia: {self.birth_date}, "
            f"adres: {self.city}, {self.street}, "
            f"{self.zip_code}, telefon: {self.phone}"
        )


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka: {self.author_name} {self.author_surname}, "
            f"data wydania: {self.publication_date}, "
            f"liczba stron: {self.number_of_pages}\n"
            f"{self.library}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_text = "\n".join(str(book) for book in self.books)

        return (
            f"Zamówienie z dnia: {self.order_date}\n"
            f"{self.employee}\n"
            f"{self.student}\n"
            f"Książki:\n{books_text}"
        )


library1 = Library(
    "Bytom", "Rynek 1", "41-902", "08:00-16:00", "111222333"
)

library2 = Library(
    "Katowice", "Szkolna 5", "40-001", "09:00-17:00", "444555666"
)

book1 = Book(library1, "2010-01-01", "Adam", "Nowak", 250)
book2 = Book(library1, "2015-05-12", "Anna", "Kowalska", 320)
book3 = Book(library2, "2020-03-15", "Jan", "Wiśniewski", 180)
book4 = Book(library2, "2018-06-20", "Maria", "Wójcik", 400)
book5 = Book(library1, "2022-09-10", "Piotr", "Mazur", 150)

employee1 = Employee(
    "Anna", "Nowak", "2020-01-01", "1990-05-12",
    "Bytom", "Polna 2", "41-902", "123456789"
)

employee2 = Employee(
    "Jan", "Kowalski", "2019-03-01", "1985-07-20",
    "Katowice", "Leśna 4", "40-001", "234567890"
)

employee3 = Employee(
    "Maria", "Mazur", "2021-06-01", "1995-02-15",
    "Bytom", "Krótka 8", "41-902", "345678901"
)

student1 = Student("Julia", [80, 90, 70])
student2 = Student("Kasia", [60, 70, 80])
student3 = Student("Adam", [40, 30, 50])

order1 = Order(
    employee1, student1, [book1, book2], "2026-01-10"
)

order2 = Order(
    employee2, student2, [book3, book4, book5], "2026-01-11"
)

print(order1)
print()
print(order2)
