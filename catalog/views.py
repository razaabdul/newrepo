from django.shortcuts import render
from .models import *
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .serializers import *
from rest_framework import viewsets



# Create your views here.

def index(request):
    num_book=book.objects.all().count()
    num_instance=BookInstance.objects.all().count()
    num_instance_avail=BookInstance.objects.filter(status__exact='a').count()
    context={
        'num_book':num_book,
        'num_instance':num_instance,
        'num_instance_avail':num_instance_avail
    }
    return render(request,'catalog_app/index.html',context=context)

class Bookcreate(LoginRequiredMixin,CreateView):
    model=book
    template_name="catalog_app/book_form.html"
    # success_url='catalog_app/book_detail/'
    fields='__all__'

# @login_required       
class book_detail(DetailView):
    model=book
    template_name="catalog_app/book_detail.html"

class sign_up(CreateView):
    form_class =UserCreationForm
    template_name='catalog_app/sign_up.html'
    success_url='/accounts/login/'


class checkedbyuser(LoginRequiredMixin,ListView):
    model=BookInstance  
    template_name='catalog_app/profile.html'
    paginate_by=5
    def get_query(self):
        return BookInstance.objects.filter(borrower=self.request.user)
     
        


class bookdetail(viewsets.ModelViewSet):

    queryset=book.objects.all()
    serializer_class=book_serializer