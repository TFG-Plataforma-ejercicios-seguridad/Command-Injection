from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('cmd',views.command_injection,name='cmd'),
    
]
