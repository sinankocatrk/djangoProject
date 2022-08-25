from django.contrib import admin
from django.urls import path
from . import views

app_name= "nick"



urlpatterns = [
    path('dashboard/', views.dashboard,name= "dashboard"),
    path('addnick/', views.addnick,name= "addnick"),    
    path('nick/<int:id>', views.detail,name= "detail"),    
]
