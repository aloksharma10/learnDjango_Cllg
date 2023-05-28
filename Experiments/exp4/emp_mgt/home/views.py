from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Employee, Department, Role

def home(request):
    return render( request,'index.html')

def all_emp(request):
    employee = Employee.objects.all()
    return render( request,'all_emp.html', {'Employee':employee})

def add_emp(request):
    Department_list = Department.objects.all()
    Role_list = Role.objects.all()
    if (request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dept = request.POST['dept']
        gender=request.POST['gender']
        role = request.POST['role']
        department1 = get_object_or_404(Department, name=dept)
        role1 = get_object_or_404(Role, name=role)
        Employee (name=name,email=email,phone=phone,dept=department1,role=role1, gender=gender).save()
        return render( request,'add_emp.html',{'Department_list':Department_list,'Role_list':Role_list})
    else:
        return render( request,'add_emp.html', {'Department_list':Department_list,'Role_list':Role_list})

def search_remove(request):
    Department_list = Department.objects.all()
    Role_list = Role.objects.all()
    employees = Employee.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        dept = request.POST['dept']
        role = request.POST['role']
        print(name, gender, dept, role)

        if name and gender and dept and role:
            filtered_employees = employees.filter(name=name, gender=gender, dept__name=dept, role__name=role)
            return render(request, 'search_remove.html', {'Department_list': Department_list, 'Role_list': Role_list, 'Employee': filtered_employees})
    
    return render(request, 'search_remove.html', {'Department_list': Department_list, 'Role_list': Role_list})


def removeemp(request, id):
    employee = get_object_or_404(Employee, eno=id)
    employee.delete()
    return render(request, 'msg.html')
