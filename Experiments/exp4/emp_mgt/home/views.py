from django.shortcuts import render

# Create your views here.
def home(request):
    return render( request,'index.html')

def all_emp(request):
    return render( request,'index.html')

def add_emp(request):
    return render( request,'index.html')

def remove_emp(request):
    return render( request,'index.html')

def filter_emp(request):
    return render( request,'index.html')

