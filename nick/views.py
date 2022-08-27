from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import NickForm
from .models import Nick
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    form = Nick.objects.filter(author=request.user)
    context = {
        "form" : form
    }
    return render(request,"dashboard.html",context)

def addnick(request):
    form = NickForm(request.POST or None,request.FILES or None)
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


def detail(request,id):
    form = get_object_or_404(Nick,id=id)


    return render(request,"detail.html",{"form": form})



def update(request,id):

    form = get_object_or_404(Nick,id=id)

    form = NickForm(request.POST or None,request.FILES or None,instance = form)
    if form.is_valid():
        nick = form.save(commit=False)
        
        nick.author = request.user
        nick.save()

        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("index")
    
    return render(request,"update.html",{"form":form})  

def delete(request,id):

    form = get_object_or_404(Nick,id=id)

    form = NickForm(request.POST or None,request.FILES or None,instance = form)
    if form.is_valid():
        nick = form.save(commit=False)
        
        nick.author = request.user
        nick.delete()

        messages.success(request,"Makale başarıyla silindi")
        return redirect("index")
    


    return render(request,"dashboard.html")




