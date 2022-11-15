from django.db import models


class Task(models.Model):
    """Модель задачи"""
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    priority = models.PositiveSmallIntegerField(default=0)

