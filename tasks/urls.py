from django.urls import path
from .views import TaskListCreateView, TaskDetailView, RegisterView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # Updated to match frontend
    path('register/', RegisterView.as_view(), name='register'),
]