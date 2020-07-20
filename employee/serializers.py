from django.contrib.auth.models import User
from rest_framework import serializers
from employee.models import Employee
from rest_framework.serializers import ModelSerializer, SerializerMethodField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = "__all__"
