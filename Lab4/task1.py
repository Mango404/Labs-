from __future__ import annotations  # ИСПРАВЛЕНИЕ 1: совместимость с Python 3.7+
from typing import Optional


class MusicalInstrument:
    """
    Базовый класс, описывающий музыкальный инструмент.

    Атрибуты:
        name (str): Название инструмента.
        brand (str): Производитель инструмента.
        _price (float): Цена инструмента.
            Непубличный, т.к. цена не должна изменяться напрямую —
            только через метод с валидацией.
        _is_tuned (bool): Настроен ли инструмент.
            Непубличный, т.к. это внутреннее состояние объекта,
            изменяемое только через метод tune().
    """

    def __init__(self, name: str, brand: str, price: float) -> None:
        """
        Инициализация музыкального инструмента.

        Args:
            name: Название инструмента.
            brand: Производитель.
            price: Цена инструмента (должна быть >= 0).

        Raises:
            ValueError: Если цена отрицательная.
        """
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.name = name
        self.brand = brand
        self._price = price
        self._is_tuned = False

    def __str__(self) -> str:
        """Возвращает удобочитаемое строковое представление инструмента."""
        status = "настроен" if self._is_tuned else "не настроен"
        return f"{self.name} ({self.brand}), цена: {self._price}₽, {status}"

    def __repr__(self) -> str:
        """Возвращает однозначное строковое представление для воссоздания объекта."""
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"brand={self.brand!r}, price={self._price!r})")

    def get_price(self) -> float:
        """
        Возвращает текущую цену инструмента.

        Returns:
            Цена инструмента.
        """
        return self._price

    def set_price(self, new_price: float) -> None:
        """
        Устанавливает новую цену инструмента с валидацией.

        Args:
            new_price: Новая цена (должна быть >= 0).

        Raises:
            ValueError: Если новая цена отрицательная.
        """
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = new_price

    def tune(self) -> str:
        """
        Настраивает инструмент (общий способ).

        Returns:
            Сообщение о результате настройки.
        """
        self._is_tuned = True
        return f"{self.name} настроен стандартным способом."

    def play(self, melody: str) -> str:
        """
        Воспроизводит мелодию на инструменте.

        Args:
            melody: Название мелодии.

        Returns:
            Сообщение о воспроизведении.
        """
        if not self._is_tuned:
            return f"{self.name} не настроен! Сначала настройте инструмент."
        return f"{self.name} играет: {melody}"

    def get_info(self) -> dict:
        """
        Возвращает словарь с основной информацией об инструменте.

        Returns:
            Словарь с полями name, brand, price, is_tuned.
        """
        return {
            "name": self.name,
            "brand": self.brand,
            "price": self._price,
            "is_tuned": self._is_tuned,
        }


class Guitar(MusicalInstrument):
    """
    Класс гитары, наследуется от MusicalInstrument.

    Дополнительные атрибуты:
        num_strings (int): Количество струн.
        guitar_type (str): Тип гитары (acoustic / electric).
        _tuning (list[str]): Текущий строй гитары.
            Непубличный, т.к. строй — внутреннее состояние,
            изменяемое только через метод tune().
    """

    STANDARD_TUNINGS: dict = {  # ИСПРАВЛЕНИЕ 4: словарь стандартных строёв
        6: ["E", "A", "D", "G", "B", "E"],
        7: ["B", "E", "A", "D", "G", "B", "E"],
        12: ["E", "E", "A", "A", "D", "D", "G", "G", "B", "B", "E", "E"],
    }

    def __init__(self, name: str, brand: str, price: float,
                 num_strings: int = 6,
                 guitar_type: str = "acoustic") -> None:
        """
        Инициализация гитары. Расширяет конструктор базового класса.

        Args:
            name: Название гитары.
            brand: Производитель.
            price: Цена.
            num_strings: Количество струн (по умолчанию 6).
            guitar_type: Тип гитары — 'acoustic' или 'electric'.

        Raises:
            ValueError: Если тип гитары не поддерживается или num_strings <= 0.
        """
        super().__init__(name, brand, price)
        if guitar_type not in ("acoustic", "electric"):
            raise ValueError("Тип гитары должен быть 'acoustic' или 'electric'.")
        if num_strings <= 0:  # ИСПРАВЛЕНИЕ 2: валидация количества струн
            raise ValueError("Количество струн должно быть положительным числом.")
        self.num_strings = num_strings
        self.guitar_type = guitar_type
        self._tuning: list = ["?"] * num_strings

    def __str__(self) -> str:
        """Удобочитаемое представление гитары с указанием типа и строя."""
        base = super().__str__()
        tuning_str = "-".join(self._tuning)
        return (f"🎸 {base}, тип: {self.guitar_type}, "
                f"струн: {self.num_strings}, строй: {tuning_str}")

    def __repr__(self) -> str:
        """Однозначное представление гитары."""
        return (f"Guitar(name={self.name!r}, brand={self.brand!r}, "
                f"price={self.get_price()!r}, "  # ИСПРАВЛЕНИЕ 5: get_price()
                f"num_strings={self.num_strings!r}, "
                f"guitar_type={self.guitar_type!r})")

    def tune(self, custom_tuning: Optional[list] = None) -> str:
        """
        Настраивает гитару в указанный или стандартный строй.

        Перегружен, т.к. настройка гитары принципиально отличается от
        общей настройки: нужно задать строй для каждой струны отдельно,
        а также поддерживается пользовательский строй (Drop D и т.д.).

        Args:
            custom_tuning: Список нот для каждой струны.
                Если None — применяется стандартный строй.

        Returns:
            Сообщение о результате настройки.

        Raises:
            ValueError: Если длина custom_tuning не совпадает с числом струн
                        или стандартный строй не найден.
        """
        if custom_tuning is not None:
            if len(custom_tuning) != self.num_strings:
                raise ValueError(
                    f"Ожидалось {self.num_strings} нот, "
                    f"получено {len(custom_tuning)}."
                )
            self._tuning = list(custom_tuning)
        else:
            # ИСПРАВЛЕНИЕ 4: проверяем наличие стандартного строя
            standard = self.STANDARD_TUNINGS.get(self.num_strings)
            if standard is None:
                raise ValueError(
                    f"Стандартный строй для {self.num_strings}-струнной "
                    f"гитары не определён. Укажите custom_tuning."
                )
            self._tuning = list(standard)

        self._is_tuned = True
        return f"{self.name} настроена в строй: {'-'.join(self._tuning)}"

    # play(), get_price(), get_info() — НАСЛЕДУЮТСЯ без изменений

    def get_tuning(self) -> list:
        """
        Возвращает текущий строй гитары.

        Returns:
            Список нот текущего строя.
        """
        return list(self._tuning)


class Piano(MusicalInstrument):
    """
    Класс фортепиано, наследуется от MusicalInstrument.

    Дополнительные атрибуты:
        num_keys (int): Количество клавиш.
        piano_type (str): Тип — 'grand' (рояль) или 'upright' (пианино).
        _last_tuned_by (str | None): Имя последнего настройщика.
            Непубличный, т.к. устанавливается только при вызове tune().
    """

    def __init__(self, name: str, brand: str, price: float,
                 num_keys: int = 88,
                 piano_type: str = "upright") -> None:
        """
        Инициализация фортепиано. Расширяет конструктор базового класса.

        Args:
            name: Название модели.
            brand: Производитель.
            price: Цена.
            num_keys: Количество клавиш (по умолчанию 88).
            piano_type: 'grand' или 'upright'.

        Raises:
            ValueError: Если тип не поддерживается или num_keys <= 0.
        """
        super().__init__(name, brand, price)
        if piano_type not in ("grand", "upright"):
            raise ValueError("Тип должен быть 'grand' или 'upright'.")
        if num_keys <= 0:  # ИСПРАВЛЕНИЕ 3: валидация количества клавиш
            raise ValueError("Количество клавиш должно быть положительным числом.")
        self.num_keys = num_keys
        self.piano_type = piano_type
        self._last_tuned_by: Optional[str] = None

    def __str__(self) -> str:
        """Удобочитаемое представление фортепиано."""
        base = super().__str__()
        kind = "Рояль" if self.piano_type == "grand" else "Пианино"
        tuner = self._last_tuned_by or "—"
        return (f"🎹 {base}, вид: {kind}, "
                f"клавиш: {self.num_keys}, настройщик: {tuner}")

    def __repr__(self) -> str:
        """Однозначное представление фортепиано."""
        return (f"Piano(name={self.name!r}, brand={self.brand!r}, "
                f"price={self.get_price()!r}, "  # ИСПРАВЛЕНИЕ 5: get_price()
                f"num_keys={self.num_keys!r}, "
                f"piano_type={self.piano_type!r})")

    def tune(self, tuner_name: str = "Автонастройка") -> str:
        """
        Настраивает фортепиано.

        Перегружен, т.к. фортепиано невозможно настроить самостоятельно —
        требуется профессиональный настройщик. Метод принимает имя
        настройщика и сохраняет его для учёта обслуживания.

        Args:
            tuner_name: Имя настройщика.

        Returns:
            Сообщение о результате настройки.
        """
        self._is_tuned = True
        self._last_tuned_by = tuner_name
        return (f"{self.name} настроено мастером «{tuner_name}». "
                f"Все {self.num_keys} клавиш звучат идеально.")

    # play(), get_price(), get_info() — НАСЛЕДУЮТСЯ без изменений

    def get_last_tuner(self) -> Optional[str]:
        """
        Возвращает имя последнего настройщика.

        Returns:
            Имя настройщика или None, если ещё не настраивался.
        """
        return self._last_tuned_by


if __name__ == "__main__":
    # === Базовый класс ===
    print("=" * 60)
    inst = MusicalInstrument("Флейта", "Yamaha", 15000)
    print(str(inst))
    print(repr(inst))
    print(inst.tune())
    print(inst.play("До-ре-ми"))
    print(inst.get_info())
    print()

    # === Guitar ===
    print("=" * 60)
    guitar = Guitar("Stratocaster", "Fender", 85000,
                     num_strings=6, guitar_type="electric")
    print(str(guitar))
    print(repr(guitar))
    print(guitar.tune())
    print(f"Строй: {guitar.get_tuning()}")
    print(guitar.tune(custom_tuning=["D", "A", "D", "G", "B", "E"]))
    print(f"Строй: {guitar.get_tuning()}")
    print(guitar.play("Stairway to Heaven"))
    print(f"Цена гитары: {guitar.get_price()}₽")
    print(f"Инфо: {guitar.get_info()}")
    print()

    # === Piano ===
    print("=" * 60)
    piano = Piano("Model D", "Steinway & Sons", 12_000_000,
                  num_keys=88, piano_type="grand")
    print(str(piano))
    print(repr(piano))
    print(piano.tune("Иванов А.С."))
    print(f"Последний настройщик: {piano.get_last_tuner()}")
    print(piano.play("Лунная соната"))
    print(f"Цена рояля: {piano.get_price()}₽")
    print(f"Инфо: {piano.get_info()}")