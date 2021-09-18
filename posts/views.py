from django.utils.text import slugify
from posts.forms import PostForm,CategoryForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Category, Post

from django.core.exceptions import *

import datetime
# Create your views here.


def post(request, slug):
    # post = Post.objects.filter(slug=slug).first()
    # return HttpResponse(f"<h1> {post.title} </h1> <br> <p> {post.content}</p>")
    post=get_object_or_404(Post,slug=slug)
    context={
        'post':post
    }
    return render(request,'post.html',context)


def index(request):
    post = Post.objects.all()
    print(post)
    return render(request,'index.html')

@login_required
def create(request):

    if request.method == 'POST':

        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author=request.user
            post = form.save()
            return redirect("post",slug=post.slug)
        # return HttpResponse(post.title)
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

@login_required
def createcategory(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        post = form.save()
        return HttpResponse(post.name)
    else:
        form = CategoryForm()
        context = {
            'form': form,
        }
        return render(request, 'createcategory.html', context)

@login_required
def update(request,slug):
    post=get_object_or_404(Post,slug=slug)

    if request.user!=post.author:
        return PermissionDenied()

    if request.method == 'POST':

        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            # form.instance.author=request.user
            post = form.save()
            return redirect('post',slug=post.slug)
        
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

@login_required
def my_posts(request):

    posts=Post.objects.filter(author=request.user)
    context={
        'posts':posts
    }

    return render(request,'posts.html',context)

@login_required
def listcategories(request):

    categories=Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,'listcategories.html',context)

@login_required
def category_posts(request,slug):
    category=get_object_or_404(Category,slug=slug)
    # print(category)
    category_id=category.id
    posts=Post.objects.filter(category_id=category_id)
    context={
        'posts':posts,
        'cat':slugify(category.name)
    }

    return render(request,'posts.html',context)

@login_required
def delete(request):

    if request.method=='POST':
        post=get_object_or_404(Post,slug=request.POST.get("slug",None))
        if request.user != post.author:
            raise PermissionDenied()

        post.deleted_at=datetime.datetime.now()
        post.save()
        return redirect("my_posts")

    else:
        raise BadRequest()





    