from django.shortcuts import render, redirect
from .models import Employee

def home(request):
    employees = Employee.objects.all()
    return render(request, "employees/home.html", {"employees": employees})


def add_employee(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email="temp@gmail.com",
            phone="1234567890",
            department="IT",
            salary=10000,
            joining_date="2026-08-07"
        )

        return redirect("home")

    return render(request, "employees/add_employee.html")
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return home(request)
def edit_employee(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        employee.first_name = request.POST["first_name"]
        employee.last_name = request.POST["last_name"]
        employee.save()
        return redirect("home")

    return render(request, "employees/edit_employee.html", {"employee": employee})