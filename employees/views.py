from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import EmployeesSerializer

from .models import Employees



@api_view(['GET'])
def employees_list(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employee(request, pk):
    employee = Employees.objects.get(id=pk)
    serializer = EmployeesSerializer(employee, many=False)
    return Response(serializer.data)
    

@api_view(['POST'])
def add_employee(request):
    serializer = EmployeesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_employee(request, pk):
    employee = Employees.objects.get(id=pk)
    serializer = EmployeesSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_employee(request, pk):
    employee = Employees.objects.get(id=pk)
    employee.delete()
    return Response('Employee deleted')