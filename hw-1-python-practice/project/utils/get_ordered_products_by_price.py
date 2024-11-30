def get_ordered_products_by_price(products):
    """
    Сортирует продукты по цене в порядке убывания.

    :param products: Список продуктов
    :return: Список продуктов, отсортированных по цене
    """
    return sorted(products, key=lambda product: product.get_price(), reverse=True)

