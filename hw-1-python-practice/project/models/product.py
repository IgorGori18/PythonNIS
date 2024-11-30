class Product:
    def __init__(self, name: str, category: str, price: float) -> None:
        """
        Инициализирует продукт.

        :param name: Название продукта
        :param category: Категория продукта
        :param price: Цена продукта
        """
        self.name: str = name
        self.category: str = category
        self.price: float = price
        self.sale: float = 0.0

    def edit_category(self, new_category: str) -> None:
        """
        Редактирует категорию продукта.

        :param new_category: Новая категория продукта
        """
        self.category = new_category

    def edit_price(self, new_price: float) -> None:
        """
        Редактирует цену продукта, если новая цена больше нуля.

        :param new_price: Новая цена продукта
        :raises ValueError: Если новая цена меньше или равна нулю
        """
        if new_price <= 0:
            raise ValueError("Price must be greater than zero.")
        self.price = new_price

    def set_sale(self, sale: float) -> None:
        """
        Устанавливает скидку на продукт.

        :param sale: Процент скидки (от 0 до 100)
        :raises ValueError: Если скидка выходит за пределы допустимого диапазона
        """
        if not (0 <= sale <= 100):
            raise ValueError("Sale must be between 0 and 100.")
        self.sale = sale

    def cancel_sale(self) -> None:
        """
        Отменяет скидку на продукт.
        """
        self.sale = 0

    def get_price(self) -> float:
        """
        Получает цену продукта с учетом скидки.

        :return: Цена продукта с учетом скидки
        """
        return self.price * (1 - self.sale / 100)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление продукта.

        :return: Строка с информацией о продукте
        """
        return (f"Product(name='{self.name}', category='{self.category}', "
                f"price={self.price}, sale={self.sale}%, final_price={self.get_price():.2f})")
