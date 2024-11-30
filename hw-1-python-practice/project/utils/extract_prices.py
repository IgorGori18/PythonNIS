def extract_prices(products):
    """
    Извлекает цены продуктов из списка.

    :param products: Список продуктов
    :return: Список цен продуктов
    """
    return [product.get_price() for product in products]
