from django.contrib import admin
from django.urls import path
from . import views
app_name='office_app'
urlpatterns = [
    path('',views.list_patients),
    path('add/',views.add,name='add'),
    path('delete/',views.delete,name='delete'),
    path('list/',views.list,name='list'),
    path('rental_review/',views.rental_review,name='rental_review'),
]
