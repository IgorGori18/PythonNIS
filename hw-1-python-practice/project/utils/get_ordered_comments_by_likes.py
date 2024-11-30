def get_ordered_comments_by_likes(comments):
    """
    Сортирует комментарии по числу лайков в порядке убывания.

    :param comments: Список комментариев
    :return: Список комментариев, отсортированных по числу лайков
    """
    return sorted(comments, key=lambda comment: comment.like_count, reverse=True)

