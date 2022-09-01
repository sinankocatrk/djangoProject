from django.contrib import admin
from django.urls import path
from . import views

app_name= "nick"



urlpatterns = [
    path('dashboard/', views.dashboard,name= "dashboard"),
    path('addnick/', views.addnick,name= "addnick"),    
    path('nick/<int:id>/', views.detail,name= "detail"), 
    path('update/<int:id>/', views.update,name= "update"),   
    path('delete/<int:id>/', views.delete,name= "delete"), 
    path('nicks/', views.nicks,name= "nicks"),  
    path('comment/<int:id>',views.addComment,name = "comment"),
]
