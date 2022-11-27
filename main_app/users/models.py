from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDERS = (
        ('Man', 'Мужчина'),
        ('Women', 'Женщина'),
    )
    GROUPS = (
        ('Backend', 'Backend разработчик'),
        ('Frontend', 'Frontend разработчик'),
        ('Tester', 'Тестировщик'),
    )

    gender = models.CharField('Пол', max_length=6, choices=GENDERS, default='')
    group = models.CharField('Специальность', max_length=10, choices=GROUPS, default=None, null=True)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'users'
