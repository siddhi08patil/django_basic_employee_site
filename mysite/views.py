from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee

def home(request):
    employees = Employee.objects.all()
    context ={
        'employees':employees
    }
    return render(request,'index.html',context)