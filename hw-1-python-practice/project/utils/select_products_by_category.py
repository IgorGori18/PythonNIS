def select_products_by_category(products, category):
    """
    Фильтрует продукты по категории.

    :param products: Список продуктов
    :param category: Категория, по которой нужно фильтровать продукты
    :return: Список продуктов, принадлежащих указанной категории
    """
    return [product for product in products if product.category == category]

