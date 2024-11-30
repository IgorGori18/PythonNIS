import uuid


class User:
    def __init__(self, name: str) -> None:
        """
        Инициализирует пользователя.

        :param name: Имя пользователя
        """
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.comments_count: int = 0
        self.rate: int = 0
        self.is_banned: bool = False

    def edit_name(self, new_name: str) -> None:
        """
        Редактирует имя пользователя.

        :param new_name: Новое имя пользователя
        """
        self.name = new_name

    def increment_rate(self) -> None:
        """
        Увеличивает рейтинг пользователя на 1.
        """
        self.rate += 1

    def ban_user(self) -> None:
        """
        Банит пользователя.
        """
        self.is_banned = True

    def unban_user(self) -> None:
        """
        Разбанивает пользователя.
        """
        self.is_banned = False

    def __repr__(self) -> str:
        """
        Возвращает строковое представление пользователя.

        :return: Строка с информацией о пользователе
        """
        return (f"User(id={self.id}, name='{self.name}', comments_count={self.comments_count}, "
                f"rate={self.rate}, is_banned={self.is_banned})")
