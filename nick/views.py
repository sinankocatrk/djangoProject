from django.shortcuts import render,HttpResponse,redirect
from .forms import NickForm
from .models import Nick
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    return render(request,"dashboard.html")

def addnick(request):
    form = NickForm(request.POST or None)
    context = {
            "form" : form
        }

    if form.is_valid():
        nick = form.save(commit=False)
        
        nick.author = request.user
        nick.save()

        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("nick:dashboard")

        


    return render(request,"addnick.html",context)



