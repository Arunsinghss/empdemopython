from django.contrib.auth.models import User
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from employee.models import Employee

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create_user(self, kwargs):
        kwargs.pop('age')
        user = User.objects.create(**kwargs)
        user.save()
        return user

    def create(self, request, *args, **kwargs):
        params = request.data if request.data else request.POST
        kwargs = {
            'first_name':  params.get('first_name', ''),
            'last_name':  params.get('last_name', ''),
            'age':  params.get('age', ''),
        }

        for key, val in kwargs.items():
            if val == '':
                return JsonResponse({"message": "Please Provide all the fields ..."}, status=400)

        kwargs.update({"username":params.get('first_name') + params.get('last_name') + str(params.get('age'))})

        try:
            user = self.create_user(kwargs)
            emp = Employee.objects.create(user=user, emp_age=params.get('age'))
            empdata = self.serializer_class(emp).data
            return JsonResponse({"message": "Employee Added Successfully...","empdata":empdata}, status=200)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)

    
    def update(self, request, pk=None, *args, **kwargs):
        try:
            params = request.data if request.data else request.POST
            kw = {}
            emp = Employee.objects.get(pk=pk)
            user = emp.user
            user.first_name = params.get('first_name')
            user.last_name = params.get('last_name')
            user.save()
            emp.emp_age = params.get('age')
            emp.save()
            empdata = self.serializer_class(emp).data
            return JsonResponse({"message": "Employee Updated Successfully...","empdata":empdata}, status=200)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
            