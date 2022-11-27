from django.db import models
from users.models import CustomUser


class Task(models.Model):
    """Модель задачи"""
    description = models.TextField('Описание задачи')
    start_date = models.DateTimeField('Начало', auto_now_add=False)
    end_date = models.DateTimeField('Завершение', auto_now_add=False)
    priority = models.PositiveSmallIntegerField('Приоритет задачи', default='')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'

    def get_absolute_url(self):
        return f'/planner/{self.pk}'

    def __str__(self):
        return f'{self.description}'


class Comment(models.Model):
    """Модель комментариев"""
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)
    text = models.CharField('', max_length=255, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def get_absolute_url(self):
        return f'/planner/{self.pk}'

    def __str__(self):
        return f'{self.task}'