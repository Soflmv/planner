from django.forms import ModelForm, Textarea, DateTimeInput, NumberInput, Select, TextInput
from .models import Task, Comment


class TaskForm(ModelForm):
    """Форма добавления новой задачи"""
    class Meta:
        model = Task
        fields = ['description', 'start_date', 'end_date', 'priority', 'user']

        widgets = {
            'description': Textarea(attrs={
                'class': 'add_task_form',
                'placeholder': 'Описание задачи',
            }),
            'start_date': DateTimeInput(attrs={
                'class': 'add_task_form',
                'placeholder': 'Дата старта',
            }),
            'end_date': DateTimeInput(attrs={
                'class': 'add_task_form',
                'placeholder': 'Дата завершения',
            }),
            'priority': NumberInput(attrs={
                'class': 'add_task_form',
                'placeholder': 'Приоритет задачи',
            }),
            'user': Select(attrs={
                'class': 'add_task_form',
            }),
        }


class CommentForm(ModelForm):
    """Форма добавления комментария"""
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': Textarea(attrs={
                'class': 'add_comment_form',
                'placeholder': 'Введите ваш комментарий',
            }),
        }