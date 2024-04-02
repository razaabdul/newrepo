from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    variable={
        'name':'abdulRaza',
        'city':'kota rajasthan',
        'user_logged_in':False
    }
    return render(request,'first_app/example.html',variable)
def variable(request):
    variable={
        'name':'abdulRaza',
        'city':'kota rajasthan',
    }
    return render(request,'first_app/variable.html',variable)
def add(request,num1,num2):
    result=num1+num2
    return HttpResponse(f"{num1} and {num2}=={result}")