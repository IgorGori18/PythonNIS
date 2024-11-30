def filter_comments_by_author(comments, author):
    """
    Фильтрует комментарии по автору.

    :param comments: Список комментариев
    :param author: Автор, чьи комментарии нужно отфильтровать
    :return: Список комментариев, написанных указанным автором
    """
    return [comment for comment in comments if comment.author_id == author.id]

