from django.shortcuts import render,HttpResponse
from .forms import NickForm
# Create your views here.
def index(request):

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    return render(request,"dashboard.html")

def addnick(request):
    form = NickForm()
    
    context = {
        "form" : form
    }
    return render(request,"addnick.html",context)



