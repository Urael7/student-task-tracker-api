from django.contrib import admin
from django.urls import path, include
from tasks.views import index
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Frontend
    path('', index, name='home'),

    # Admin
    path('admin/', admin.site.urls),

    # Task API routes (tasks, register)
    path('api/', include('tasks.urls')),

    # JWT Authentication
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]