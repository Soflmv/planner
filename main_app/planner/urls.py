from django.urls import path
from . import views

urlpatterns = [
    path('all_tasks/', views.tasks, name='all_tasks'),
    path('new_task/', views.new_task, name='new_task'),
    path('add_task/', views.new_task, name='add_task'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/add_comments/', views.add_comments, name='add_comments'),
]
