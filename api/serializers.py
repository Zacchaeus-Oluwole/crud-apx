from django.db.models import fields
from rest_framework import serializers
from crud_app.models import Employee

class EmployeeApi(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('eid', 'ename', 'eemail', 'econtact')