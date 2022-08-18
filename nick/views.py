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
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        nick=Nick()
        nick.title=title
        nick.content=content
        nick.author = request.user
        nick.save()
        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("nick:dashboard")

        


    return render(request,"addnick.html",context)



