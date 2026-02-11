# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union, Literal
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass



class Book:
    def __init__(self, title: str, total_pages: int, current_page: int = 0):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param total_pages: Общее количество страниц
        :param current_page: Текущая страница (по умолчанию 0 — книга не открыта)

        Примеры:
        >>> book = Book("Война и мир", 1225)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if len(title.strip()) == 0:
            raise ValueError("Название книги не может быть пустой строкой")
        self.title = title

        if not isinstance(total_pages, int):
            raise TypeError("Общее количество страниц должно быть типа int")
        if total_pages <= 0:
            raise ValueError("Общее количество страниц должно быть положительным числом")
        self.total_pages = total_pages

        if not isinstance(current_page, int):
            raise TypeError("Номер текущей страницы должен быть типа int")
        if current_page < 0:
            raise ValueError("Номер текущей страницы не может быть отрицательным")
        if current_page > total_pages:
            raise ValueError("Номер текущей страницы не может превышать общее количество страниц")
        self.current_page = current_page

    def is_finished(self) -> bool:
        """
        Проверяет, прочитана ли книга до конца.

        :return: True, если текущая страница равна общему числу страниц, иначе False

        Примеры:
        >>> book = Book("Война и мир", 1225, 1225)
        >>> book.is_finished()
        True
        """
        ...

    def turn_pages(self, pages: int) -> None:
        """
        Перелистывание страниц вперёд.

        :param pages: Количество страниц для перелистывания
        :raise ValueError: Если количество страниц отрицательное или выходит за пределы книги

        Примеры:
        >>> book = Book("Война и мир", 1225, 0)
        >>> book.turn_pages(50)
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц для перелистывания не может быть отрицательным")
        if self.current_page + pages > self.total_pages:
            raise ValueError("Нельзя перелистнуть дальше последней страницы")
        ...

    def get_reading_progress(self) -> float:
        """
        Возвращает прогресс чтения в процентах.

        :return: Процент прочитанных страниц (от 0.0 до 100.0)

        Примеры:
        >>> book = Book("Война и мир", 1225, 612)
        >>> book.get_reading_progress()
        49.96
        """
        ...


class BankAccount:
    def __init__(self, owner: str, balance: float, annual_rate: float):
        """
        Создание и подготовка к работе объекта "Банковский счёт"

        :param owner: Имя владельца счёта
        :param balance: Баланс счёта
        :param annual_rate: Годовая процентная ставка (в процентах, например 5.0)

        Примеры:
        >>> account = BankAccount("Иван Иванов", 10000.0, 5.0)  # инициализация экземпляра класса
        """
        if not isinstance(owner, str):
            raise TypeError("Имя владельца должно быть строкой")
        if len(owner.strip()) == 0:
            raise ValueError("Имя владельца не может быть пустой строкой")
        self.owner = owner

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть типа int или float")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = balance

        if not isinstance(annual_rate, (int, float)):
            raise TypeError("Процентная ставка должна быть типа int или float")
        if annual_rate < 0:
            raise ValueError("Процентная ставка не может быть отрицательной")
        self.annual_rate = annual_rate

    def deposit(self, amount: float) -> None:
        """
        Пополнение счёта.

        :param amount: Сумма пополнения
        :raise ValueError: Если сумма пополнения не положительная

        Примеры:
        >>> account = BankAccount("Иван Иванов", 10000.0, 5.0)
        >>> account.deposit(5000.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма пополнения должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительным числом")
        ...

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств со счёта.

        :param amount: Сумма снятия
        :raise ValueError: Если сумма снятия превышает текущий баланс или не положительная

        Примеры:
        >>> account = BankAccount("Иван Иванов", 10000.0, 5.0)
        >>> account.withdraw(3000.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма снятия должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительным числом")
        if amount > self.balance:
            raise ValueError("Сумма снятия не может превышать текущий баланс")
        ...

    def calculate_annual_interest(self) -> float:
        """
        Рассчитывает сумму начисленных процентов за год.

        :return: Сумма процентов за год

        Примеры:
        >>> account = BankAccount("Иван Иванов", 10000.0, 5.0)
        >>> account.calculate_annual_interest()
        500.0
        """
        ...


class Playlist:
    def __init__(self, name: str, max_tracks: int):
        """
        Создание и подготовка к работе объекта "Плейлист"

        :param name: Название плейлиста
        :param max_tracks: Максимальное количество треков в плейлисте

        Примеры:
        >>> playlist = Playlist("Мой плейлист", 100)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название плейлиста должно быть строкой")
        if len(name.strip()) == 0:
            raise ValueError("Название плейлиста не может быть пустой строкой")
        self.name = name

        if not isinstance(max_tracks, int):
            raise TypeError("Максимальное количество треков должно быть типа int")
        if max_tracks <= 0:
            raise ValueError("Максимальное количество треков должно быть положительным числом")
        self.max_tracks = max_tracks

        self.tracks: list[str] = []

    def add_track(self, track_name: str) -> None:
        """
        Добавление трека в плейлист.

        :param track_name: Название добавляемого трека
        :raise ValueError: Если плейлист уже заполнен до максимума или название трека пустое

        Примеры:
        >>> playlist = Playlist("Мой плейлист", 100)
        >>> playlist.add_track("Bohemian Rhapsody")
        """
        if not isinstance(track_name, str):
            raise TypeError("Название трека должно быть строкой")
        if len(track_name.strip()) == 0:
            raise ValueError("Название трека не может быть пустой строкой")
        if len(self.tracks) >= self.max_tracks:
            raise ValueError("Плейлист заполнен, невозможно добавить новый трек")
        ...

    def remove_track(self, track_name: str) -> None:
        """
        Удаление трека из плейлиста по названию.

        :param track_name: Название удаляемого трека
        :raise ValueError: Если трека с таким названием нет в плейлисте

        Примеры:
        >>> playlist = Playlist("Мой плейлист", 100)
        >>> playlist.add_track("Bohemian Rhapsody")
        >>> playlist.remove_track("Bohemian Rhapsody")
        """
        if not isinstance(track_name, str):
            raise TypeError("Название трека должно быть строкой")
        ...

    def is_empty(self) -> bool:
        """
        Проверяет, является ли плейлист пустым.

        :return: True, если в плейлисте нет треков, иначе False

        Примеры:
        >>> playlist = Playlist("Мой плейлист", 100)
        >>> playlist.is_empty()
        True
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации