from django.shortcuts import render
from rest_framework import generics
from django.utils import timezone
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from .models import Task
from .serializers import TaskSerializer, UserRegisterSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    filterset_fields = ['status', 'priority']
    ordering_fields = ['deadline', 'created_at']

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        overdue = self.request.query_params.get('overdue')

        if overdue == 'true':
            queryset = queryset.filter(
                deadline__lt=timezone.now(),
                status='pending'
            )

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


def index(request):
    return render(request, 'index.html')