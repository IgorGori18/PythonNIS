def select_top_users_by_rate(users, top_size):
    """
    Выбирает топ N пользователей по рейтингу.

    :param users: Список пользователей
    :param top_size: Количество пользователей для вывода
    :return: Список топ N пользователей по рейтингу
    """
    return sorted(users, key=lambda user: user.rate, reverse=True)[:top_size]

