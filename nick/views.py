from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

import nick
from .forms import NickForm
from .models import Nick,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):

    keyword = request.GET.get("keyword")

    if keyword :
        articles = Nick.objects.filter(title__contains = keyword)
        return render(request,"index.html",{"articles":articles})

    articles = Nick.objects.filter()
    context = {
        "articles" : articles
    }
    return render(request,"index.html",context)


def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    form = Nick.objects.filter(author=request.user)
    context = {
        "form" : form
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
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

@login_required(login_url="user:login")
def detail(request,id):
    nick = get_object_or_404(Nick,id=id)
    comments = nick.comments.all()
    print(comments)
    return render(request,"detail.html",{"nick":nick,"comments":comments})


@login_required(login_url="user:login")
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
@login_required(login_url="user:login")
def delete(request,id):

    form = get_object_or_404(Nick,id=id)
    form.delete()

    messages.success(request,"Makale başarıyla silindi")

    
    return redirect("nick:dashboard")

@login_required(login_url="user:login")
def nicks(request):
    keyword = request.GET.get("keyword")

    if keyword :
        articles = Nick.objects.filter(title__contains = keyword)
        return render(request,"nicks.html",{"articles":articles})

    articles = Nick.objects.filter()
    context = {
        "articles" : articles
    }
    return render(request,"nicks.html",context)


def addComment(request,id):
    nick = get_object_or_404(Nick,id = id)

    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.nick = nick

        newComment.save()
    return redirect(reverse("nick:detail",kwargs={"id":id}))
    




