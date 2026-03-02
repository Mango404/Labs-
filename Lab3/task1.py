class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Название книги (только для чтения)."""
        return self._name

    @property
    def author(self) -> str:
        """Автор книги (только для чтения)."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Бумажная книга. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # используем сеттер для проверки

    @property
    def pages(self) -> int:
        """Количество страниц (целое положительное число)."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self):
        # Добавляем информацию о страницах к базовому строковому представлению
        return f"{super().__str__()} – {self.pages} стр."

    def __repr__(self):
        # Полное представление для воссоздания объекта
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages!r})")


class AudioBook(Book):
    """ Аудиокнига. """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # используем сеттер для проверки

    @property
    def duration(self) -> float:
        """Длительность аудиокниги в часах (положительное число)."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        # Разрешаем передачу int, но храним как float
        if not isinstance(value, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")
        self._duration = float(value)

    def __str__(self):
        # Добавляем информацию о длительности
        return f"{super().__str__()} – {self.duration} ч."

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration!r})")