from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm()
    context = {
        "form":form
    }
    return render(request,"register.html",context)

def loginUser(request):
    return render(request,"login.html")

def logoutUser(request):
    pass



