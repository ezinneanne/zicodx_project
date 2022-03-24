from      django.urls import path  #importing the necessary documents
from . import views 

app_name ='zicodxapp'

urlpatterns = [
  path('', views.index, name='index'),
]
