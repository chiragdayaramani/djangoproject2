from django.utils.text import slugify
from posts.forms import PostForm,CategoryForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Category, Post

from django.core.exceptions import *
from django.core.paginator import Paginator
import datetime

from django.db.models import Q
# Create your views here.


def post(request, slug):
    # post = Post.query.filter(slug=slug).first()
    # return HttpResponse(f"<h1> {post.title} </h1> <br> <p> {post.content}</p>")
    post=get_object_or_404(Post,slug=slug)
    post.increment_views()
    context={
        'post':post
    }
    return render(request,'post.html',context)


def index(request):
    latest_posts=Post.query.all().order_by("-created_at")[:6]
    trending_posts=Post.query.all().order_by("-views")[:3]

    context={
        'latest_posts':latest_posts,
        'trending_posts':trending_posts
    }

    return render(request,'index.html',context)

@login_required
def create(request):

    if request.method == 'POST':

        form = PostForm(request.POST,request.FILES)
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

        form = PostForm(request.POST,request.FILES,instance=post)
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

    posts=Post.query.filter(author=request.user)
    paginator=Paginator(posts,2)
    is_paginated=paginator.num_pages>1
    page=request.GET.get("page",1)
    if int(page) > paginator.num_pages:
        page=1
    page_obj=paginator.page(page)

    context={
        'is_paginated':is_paginated,
        'page_obj':page_obj,  
    }

    return render(request,'posts.html',context)

@login_required
def search(request):
    search=request.GET.get("search","")
    posts=Post.query.filter(Q(title__icontains=search) | Q(content__icontains=search))

    context={
        'is_paginated':False,
        'page_obj':posts,  
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





@login_required
def trash(request):

    posts=Post.objects.filter(author=request.user).exclude(deleted_at=None)
    context={
        'posts':posts
    }

    return render(request,'trash.html',context)


@login_required
def restore(request,slug):
    if request.method=='GET':
        post=get_object_or_404(Post.objects,slug=slug)
        if request.user!=post.author:
            raise PermissionDenied()
        
        post.deleted_at=None
        post.save()
        return redirect('my_posts')
    else:
        raise BadRequest()


def permanent_delete(request):
    if request.method=='POST':
        post=get_object_or_404(Post.objects,slug=request.POST.get("slug",None))
        if request.user!=post.author:
            raise PermissionDenied()
        post.delete()
        return redirect('my_posts')
    else:
        raise BadRequest()