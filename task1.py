from typing import Optional


class PaymentCard:
    """
    Базовый класс, представляющий банковскую платёжную карту.

    Attributes:
        card_number (str): Номер карты.
        owner (str): Владелец карты.
        balance (float): Баланс карты.
    """

    def __init__(self, card_number: str, owner: str, balance: float) -> None:
        """
        Инициализация платёжной карты.

        Args:
            card_number (str): Номер карты.
            owner (str): Имя владельца.
            balance (float): Начальный баланс.
        """
        self.card_number = card_number
        self.owner = owner
        self._balance = balance  # защищённый атрибут, изменение должно происходить только через методы

    def __str__(self) -> str:
        """Строковое представление карты для пользователя."""
        return f"PaymentCard(owner={self.owner}, balance={self._balance})"

    def __repr__(self) -> str:
        """Строковое представление объекта для разработчиков."""
        return f"PaymentCard(card_number={self.card_number}, owner={self.owner}, balance={self._balance})"

    def deposit(self, amount: float) -> None:
        """
        Пополнение баланса карты.

        Args:
            amount (float): Сумма пополнения.
        """
        pass

    def withdraw(self, amount: float) -> bool:
        """
        Снятие средств с карты.

        Args:
            amount (float): Сумма снятия.

        Returns:
            bool: True, если операция выполнена успешно.
        """
        pass

    def get_balance(self) -> float:
        """
        Получить текущий баланс карты.

        Returns:
            float: Текущий баланс.
        """
        return self._balance


class CreditCard(PaymentCard):
    """
    Дочерний класс кредитной карты.

    Расширяет функциональность обычной платёжной карты,
    добавляя кредитный лимит.

    Attributes:
        credit_limit (float): Максимальный кредитный лимит.
    """

    def __init__(self, card_number: str, owner: str, balance: float, credit_limit: float) -> None:
        """
        Инициализация кредитной карты.

        Args:
            card_number (str): Номер карты.
            owner (str): Имя владельца.
            balance (float): Начальный баланс.
            credit_limit (float): Кредитный лимит.
        """
        super().__init__(card_number, owner, balance)
        self.credit_limit = credit_limit

    def __str__(self) -> str:
        """Строковое представление кредитной карты."""
        return f"CreditCard(owner={self.owner}, balance={self._balance}, credit_limit={self.credit_limit})"

    def __repr__(self) -> str:
        """Представление объекта для разработчиков."""
        return (
            f"CreditCard(card_number={self.card_number}, "
            f"owner={self.owner}, balance={self._balance}, credit_limit={self.credit_limit})"
        )

    def withdraw(self, amount: float) -> bool:
        """
        Снятие средств с кредитной карты.

        Метод перегружен, потому что кредитная карта позволяет
        уходить в отрицательный баланс в пределах кредитного лимита.

        Args:
            amount (float): Сумма снятия.

        Returns:
            bool: True, если операция выполнена.
        """
        pass

    def available_credit(self) -> float:
        """
        Рассчитать доступный кредит.

        Returns:
            float: Сумма доступного кредита.
        """
        pass


if __name__ == "__main__":
    # Write your solution here
    pass