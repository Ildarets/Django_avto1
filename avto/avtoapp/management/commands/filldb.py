from django.core.management.base import BaseCommand
from avtoapp.models import Category, Post, Tag


# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Выбираем ВСЕ категории
        categories = Category.objects.all()
        print(categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(item.name)
            print(type(item))

        print('End')

        # Выбрать ОДНУ категорию
        category = Category.objects.get(name='Москва')
        print(category)
        print(type(category))

        # Несколько
        category = Category.objects.filter(name='Питер')
        print(category)
        print(type(category))

        # Первый пост
        post = Post.objects.first()

        print(post)

        # Связанные поля
        # ForeignKey
        print(post.category)
        print(type(post.category))
        print(post.category.name)
        # ManyToMany
        print(post.tags.all())
        print(post.tags.first())
        print(post.tags.first().name)
        print(type(post.tags.first()))
        print(post.tags.filter(name='Небитый'))

        # Создание
        # Category.objects.create(name='Новая', description='Что то')

        # Изменение
        category = Category.objects.get(name='Измененная')
        # category.name = 'Измененная'
        # category.save()

        # Удаление
        # Можно одну,
        category.delete()
        # # можно несколько
        # # Category.objects.all().delete()