from django.db import models


class Task(models.Model):
    """Модель задачи"""
    description = models.TextField('Описание задачи')
    start_date = models.DateTimeField('Начало', auto_now_add=False)
    end_date = models.DateTimeField('Завершение', auto_now_add=False)
    priority = models.PositiveSmallIntegerField('Приоритет задачи', default=0)

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.description}'
