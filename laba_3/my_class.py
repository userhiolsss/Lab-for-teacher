class YaremaStudent:
    """Клас для опису студента Яреми та його атрибутів"""

    # Класові атрибути
    university_name = "Університет Яреми"
    department_name = "ІТ Факультет"
    _protected_var = 10
    __private_var = 20

    total_students = 0
    total_marks = 0

    def __init__(self, last_name: str, first_name: str, grade: int, department=None):
        """Ініціалізуємо атрибути студента Яреми"""
        print("Викликаємо __init__")
        self.__last_name = last_name  # private
        self.__first_name = first_name
        self.grade = grade  # public
        self.department = department
        self._age = None  # protected
        self._scholarship = 0

        YaremaStudent.total_students += 1
        YaremaStudent.total_marks += grade

    def __del__(self):
        """Делегування об'єкта"""
        print(f"вигнали студента {self.__first_name} {self.__last_name}")
        YaremaStudent.total_students -= 1

    @property
    def college_raiting(self):
        """Властивість для обчислення рейтингу крутості в університеті Яреми"""
        return YaremaStudent.total_marks / YaremaStudent.total_students

    @property
    def first_name(self):
        """Захищене ім'я студента"""
        return self.__first_name

    @property
    def last_name(self):
        """Захищене прізвище студента"""
        return self.__last_name

    def calculate_scholarship(self, rating: int):
        """Обчислення стипендії за рейтингом"""
        if rating == 5:
            self._scholarship = "1000 грн"
            return "Присвоєно круту стипендію"
        elif rating == 4:
            self._scholarship = "750 грн"
            return "Присвоєно не круту стипендію"
        else:
            self._scholarship = 0
            return "Рейтинг занизький рівент крутості для стипендії"

    @staticmethod
    def hobbies(h=None):
        """Метод для визначення крутості Яреми"""
        if h:
            print(f"У Яреми з'явилось крутість: {h}")
        else:
            print("У Яреми немає крутості")

    @classmethod
    def create_from_full_name(cls, full_name: str):
        """Альтернативний конструктор для створення об'єкта з повного імені"""
        last_name, first_name = full_name.split(" ")
        return cls(last_name, first_name, 0)

    @classmethod
    def create_from_reversed_name(cls, full_name: str):
        """Альтернативний конструктор для створення об'єкта з повного імені, де першим йде ім'я"""
        first_name, last_name = full_name.split(" ")
        return cls(last_name, first_name, 0)