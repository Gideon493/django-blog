from multiprocessing import context
from re import template
from unittest import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Members, Blog
from . import forms
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def hello(request):
    return render(request, 'home.html')

# Create your views here.


@login_required(login_url="/accounts/login/")
def members_list(request):
    mymembers = Members.objects.all()
    return render(request, 'members.html', {'mymembers': mymembers})


def members_detail(request, firstname):
    member = Members.objects.get(firstname=firstname)
    return render(request, 'member_detail.html', {'member': member})


def blog_article_view(request):
    articles = Blog.objects.all()
    """if request.method == 'POST':
        
        instance = articles.save(commit = False)
        instance.author = request.user
        instance.save()
        return redirect('/playground/')
    else:
        articles = forms.CreateBlog()"""
    return render(request, 'articles.html', {'articles': articles})


def article_detail_view(request, title):
    article = Blog.objects.get(title=title)
    return render(request, 'article_detail.html', {'article': article})


def create_blog_view(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('/playground/articles/')
    else:
        form = forms.CreateBlog()
    return render(request, 'create_blog.html', {'form': form})
