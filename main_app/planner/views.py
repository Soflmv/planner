from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Task, Comment
from .forms import TaskForm, CommentForm


def tasks(request):
    """Все задачи"""
    data = Task.objects.order_by('-priority')
    return render(request, 'planner/home.html', {'data': data})


def new_task(request):
    """Создать новую задачу"""
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
        else:
            error = 'Форма была заполнена некорректно'

    form = TaskForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'planner/add_task.html', data)


def add_comments(request, pk):
    """Добавление комментариев к задачам"""
    new = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.task_id = pk
            form.user = request.user
            form.new = new
            form.save()
            return redirect('add_comments', pk)
    else:
        form = CommentForm()
        comment = Comment.objects.filter(task=pk)

    return render(request,
                  'planner/comments.html',
                  {'new': new,
                   'comment': comment,
                   'form': form})


class TaskDetailView(DetailView):
    """Просмотреть задачу детально"""
    model = Task
    template_name = 'planner/task_detail.html'
    context_object_name = 'detail'


class TaskUpdateView(UpdateView):
    """Редактировать задачу"""
    model = Task
    template_name = 'planner/add_task.html'
    form_class = TaskForm
    success_url = '/planner/all_tasks/'


class TaskDeleteView(DeleteView):
    """Удалить задачу"""
    model = Task
    success_url = '/planner/all_tasks/'
    template_name = 'planner/task_delete.html'
