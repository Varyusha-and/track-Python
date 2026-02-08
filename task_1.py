from abc import ABC, abstractmethod
from typing import Any
import doctest


class Furniture(ABC):
    """
    Абстрактный класс, описывающий предмет мебели.
    """

    def __init__(self, material: str, weight: float):
        """
        :param material: Материал, из которого изготовлена мебель
        :param weight: Вес мебели в килограммах

        Ограничения:
        - material не может быть пустой строкой
        - weight должен быть положительным числом
        """
        if not material:
            raise ValueError("Материал не может быть пустым")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным")

        self.material: str = material
        self.weight: float = weight

    @abstractmethod
    def move(self, distance: float) -> None:
        """
        Перемещает мебель на заданное расстояние.

        :param distance: Расстояние в метрах
        :return: None

        Ограничения:
        - distance должен быть больше 0

        >>> class Chair(Furniture):
        ...     def move(self, distance: float) -> None:
        ...         pass
        ...     def assemble(self) -> None:
        ...         pass
        >>> chair = Chair("wood", 5.0)
        >>> chair.move(2.0)
        """
        ...

    @abstractmethod
    def assemble(self) -> None:
        """
        Сборка мебели.

        :return: None

        >>> class Table(Furniture):
        ...     def move(self, distance: float) -> None:
        ...         pass
        ...     def assemble(self) -> None:
        ...         pass
        >>> table = Table("metal", 10.0)
        >>> table.assemble()
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс, описывающий дерево как живой объект.
    """

    def __init__(self, age: int, height: float):
        """
        :param age: Возраст дерева в годах
        :param height: Высота дерева в метрах

        Ограничения:
        - age не может быть отрицательным
        - height должна быть больше 0
        """
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if height <= 0:
            raise ValueError("Высота должна быть больше нуля")

        self.age: int = age
        self.height: float = height

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева.

        :param years: Количество лет
        :return: None

        Ограничения:
        - years должен быть положительным числом

        >>> class Oak(Tree):
        ...     def grow(self, years: int) -> None:
        ...         pass
        ...     def produce_oxygen(self) -> float:
        ...         return 1.0
        >>> oak = Oak(10, 3.5)
        >>> oak.grow(5)
        """
        ...

    @abstractmethod
    def produce_oxygen(self) -> float:
        """
        Производит кислород.

        :return: Количество произведённого кислорода в условных единицах

        >>> class Pine(Tree):
        ...     def grow(self, years: int) -> None:
        ...         pass
        ...     def produce_oxygen(self) -> float:
        ...         return 2.5
        >>> pine = Pine(20, 6.0)
        >>> pine.produce_oxygen()
        2.5
        """
        ...


class SocialNetwork(ABC):
    """
    Абстрактный класс, описывающий социальную сеть как нематериальный объект.
    """

    def __init__(self, name: str, users_count: int):
        """
        :param name: Название социальной сети
        :param users_count: Количество пользователей

        Ограничения:
        - name не может быть пустым
        - users_count не может быть отрицательным
        """
        if not name:
            raise ValueError("Название не может быть пустым")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")

        self.name: str = name
        self.users_count: int = users_count

    @abstractmethod
    def register_user(self, user_id: Any) -> None:
        """
        Регистрирует нового пользователя.

        :param user_id: Идентификатор пользователя
        :return: None

        >>> class Facebook(SocialNetwork):
        ...     def register_user(self, user_id: Any) -> None:
        ...         pass
        ...     def post_content(self, content: str) -> bool:
        ...         return True
        >>> fb = Facebook("Facebook", 100)
        >>> fb.register_user("user_1")
        """
        ...

    @abstractmethod
    def post_content(self, content: str) -> bool:
        """
        Публикует контент.

        :param content: Текст публикации
        :return: Успешность публикации

        Ограничения:
        - content не должен быть пустым

        >>> class VK(SocialNetwork):
        ...     def register_user(self, user_id: Any) -> None:
        ...         pass
        ...     def post_content(self, content: str) -> bool:
        ...         return True
        >>> vk = VK("VK", 50)
        >>> vk.post_content("Hello")
        True
        """
        ...


if __name__ == "__main__":
    doctest.testmod()