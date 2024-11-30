from datetime import datetime
from typing import Optional

class Comment:
    def __init__(self, author_id: str, text: str) -> None:
        """
        Инициализирует комментарий.

        :param author_id: ID автора комментария
        :param text: Текст комментария
        """
        self.author_id: str = author_id
        self.text: str = text
        self.create_data: datetime = datetime.now()
        self.update_data: datetime = self.create_data
        self.like_count: int = 0

    def edit_comment(self, new_text: str) -> None:
        """
        Редактирует комментарий, обновляя его текст.

        :param new_text: Новый текст комментария
        """
        self.text = new_text
        self.update_data = datetime.now()

    def like(self) -> None:
        """
        Увеличивает количество лайков на 1.
        """
        self.like_count += 1

    def dislike(self) -> None:
        """
        Уменьшает количество лайков на 1.
        """
        self.like_count -= 1

    def __repr__(self) -> str:
        """
        Представление комментария в виде строки.

        :return: Строковое представление комментария
        """
        return (f"Comment(author_id={self.author_id}, text='{self.text}', "
                f"likes={self.like_count}, created={self.create_data}, updated={self.update_data})")
