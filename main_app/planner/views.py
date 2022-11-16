from django.shortcuts import render
from .models import Task


def main(request):
    data = Task.objects.order_by('-priority')
    return render(request, 'planner/home.html', {'data': data})
