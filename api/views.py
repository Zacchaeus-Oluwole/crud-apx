
from rest_framework import generics
from crud_app.models import Employee
from .serializers import EmployeeApi

# Create your views here.


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeApi

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeApi