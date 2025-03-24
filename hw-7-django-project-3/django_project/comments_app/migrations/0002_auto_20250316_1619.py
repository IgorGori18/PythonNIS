from django.db import migrations
from django.utils import timezone


def create_mock_data(apps, schema_editor):
    User = apps.get_model('comments_app', 'User')
    Post = apps.get_model('comments_app', 'Post')
    Comment = apps.get_model('comments_app', 'Comment')

    # Создаем пользователя
    user = User.objects.create(username='mockuser', email='mock@example.com')

    # Создаем пост
    post = Post.objects.create(
        author=user,
        title='Мок-пост',
        content='Содержимое мок-поста',
        created_at=timezone.now()
    )

    # Создаем комментарий
    Comment.objects.create(
        post=post,
        author=user,
        content='Мок-комментарий',
        created_at=timezone.now()
    )


class Migration(migrations.Migration):
    dependencies = [
        ('comments_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_mock_data),
    ]
