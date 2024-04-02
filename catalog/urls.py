from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *
from rest_framework import routers


routers=routers.DefaultRouter()
routers.register('detail_book/',views.bookdetail)
urlpatterns=[
    path('',include(routers.urls)),
    path('index/',views.index),
    path('create_book/',views.Bookcreate.as_view(),name='create_book'),
    path('book_detail/<int:pk>/',views.book_detail.as_view(),name='book_detail'),
    path('signup/',views.sign_up.as_view(),name='sign_up'),
    path('profile/',views.checkedbyuser.as_view(),name='profile')



]