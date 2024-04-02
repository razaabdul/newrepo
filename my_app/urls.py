from django.urls import path
from . import views
app_name='my_app'
urlpatterns = [
    path('home/', views.index,name='variable'),
    path('variable/',views.variable,name='variables'),
    path('<int:num1>/<int:num2>', views.add),
]
