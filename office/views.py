from django.shortcuts import render,redirect
from . import models
from django.urls import reverse
from . forms import reviewform

# Create your views here.
def list_patients(request):
    query=models.patient.objects.all()
    context={
        'data':query
    }
    return render(request,'office_app/List.html',context)

def add(request):
    if request.method=="POST":
        brand=request.POST.get('brand')
        year=request.POST.get('year')
        models.car.objects.create(brand=brand,year=year)
        return redirect('office_app:list')
    return render(request,'office_app/add.html')


def list(request):
    query=models.car.objects.all()
    context={
        'data':query
    }
    return render(request,'office_app/list.html',context)

def delete(request):
    if request.method=='POST':
         
        pk=request.POST['pk']
        try:
            models.car.objects.get(pk=pk).delete()
        except:
             print ('pk notfound ')
             return redirect('office_app:list')
    return render(request,'office_app/delete.html')

def rental_review(request):
    if request.method=='POST':
        form=reviewform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('office_app:rental_review')
    else:
        form = reviewform()
    return render(request,'office_app/rental_review.html',context={'form':form})