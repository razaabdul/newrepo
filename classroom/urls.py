from django.urls import path
from .views import *

# app_name='classroom'  
urlpatterns=[
    path('',homeview.as_view(),name='home'),
    path('thanku_page/',thanku.as_view(),name='thanku_page'),
    path('contact_form/',contactform.as_view(),name='contact_form'),
    path('teacher/',teacher_form.as_view(),name='teacher'),
    path('list_teacher/',teacher_list.as_view(),name='list_teacher'),
    path('teacher_detail/<int:pk>',teacher_detail.as_view(),name='teacher_detail'),
    path('update_teacher/<int:pk>',update_teacher.as_view(),name='update_teacher'),
    path('delete_view/<int:pk>',delete_view.as_view(),name='delete_view'),




]      