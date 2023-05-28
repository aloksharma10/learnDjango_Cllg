from django.shortcuts import render

# Create your views here.
def home(request):
    return render( request,'index.html')

def all_emp(request):
    return render( request,'all_emp.html')

def add_emp(request):
    return render( request,'add_emp.html')

def search_remove(request):
    return render( request,'filter_emp.html')

