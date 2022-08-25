from rest_framework import viewsets, routers
from django.urls import path, include
from .models import Employees
from .serializers import EmployeesSerializer
from . import views


urlpatterns = [
    path('', views.employees_list),
    path('employee/<str:pk>', views.get_employee),
    path('update-employee/<str:pk>', views.update_employee),
    path('delete-employee/<str:pk>', views.delete_employee),
    path('add-employee/', views.add_employee),
]