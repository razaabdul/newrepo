from django.shortcuts import render
from django.views.generic import TemplateView,FormView,ListView,DetailView,UpdateView,DeleteView #Renders a given template,FormView
from classroom.forms import *
from .models import *
class homeview(TemplateView):
    template_name='classroom_app/home.html'

class thanku(TemplateView):
    template_name='classroom_app/thanku.html'

class contactform(FormView):
        form_class = contactform  # Use form_class attribute to assign the form class
        template_name = 'classroom_app/contact_form.html' # where you wanna sent to form
        # query=contact_info.objects.all()
        # print(query) 
        # print("====>")
        #url not template
        success_url = '/classroom/thanku_page/'
        def form_valid(self, form):
        # Save the form data to the database
            form.save()
        # Call the parent class's form_valid method to handle the success URL redirection
            return super().form_valid(form)   # inheriting from form FormView

class teacher_form(FormView):
    form_class=teacher_info
    template_name='classroom_app/teacher_form.html'     
    success_url='/classroom/thanku_page/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
class teacher_list(ListView):
    model=teacher
    template_name='classroom_app/list_teacher.html' 
    # query=teacher.objects.order_by('last_name')

    context="teacher_list"     #you can iterate value also by using this name


# show models single column data
class teacher_detail(DetailView):
     model=teacher
     #pk={{teacher}}
     template_name='classroom_app/teacher_detail.html'
class update_teacher(UpdateView):
     model=teacher
     fields='__all__'
     template_name='classroom_app/teacher_form.html'
     success_url ='/classroom/list_teacher/'

class delete_view(DeleteView):
     model=teacher
     fields='__all__'
     template_name='classroom_app/delete_data.html'
     success_url ='/classroom/list_teacher/'

