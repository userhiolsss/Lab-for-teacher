class Book:
    """Клас для опису книги."""

    # Атрибути класу
    total_books = 0  # загальна кількість книг

    def __init__(self, title, author, year):
        """Ініціалізація атрибутів книги."""
        self.title = title  # назва книги
        self.author = author  # автор книги
        self.year = year  # рік публікації книги
        Book.total_books += 1  # збільшення лічильника книг

    def __str__(self):
        """Метод для виведення інформації про книгу."""
        return f"'{self.title}' by {self.author} ({self.year})"

    @classmethod
    def get_total_books(cls):
        """Метод класу для отримання кількості книг."""
        return cls.total_books

    @staticmethod
    def is_readable():
        """Статичний метод, який визначає, чи можна прочитати книгу."""
        return True


# Створення об'єктів класу
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Виведення інформації про книги
print(book1)
print(book2)

# Виведення кількості створених книг
print(f"Загальна кількість книг: {Book.get_total_books()}")

# Виклик статичного методу
print(f"Чи можна прочитати книгу: {Book.is_readable()}")