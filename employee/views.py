from django.shortcuts import render,get_object_or_404
from employee.models import Employee
from django.http import HttpResponse

# Create your views here.
def employee_details(request,pk):

        employee=get_object_or_404(Employee , pk=pk)
        context ={
                'employee':employee,
        } 
        return render(request,'employee_details.html',context)

