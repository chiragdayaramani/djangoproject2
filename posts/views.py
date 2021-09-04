from posts.forms import PostForm,CategoryForm
from django.shortcuts import render, HttpResponse
from .models import Category, Post
# Create your views here.


def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return HttpResponse(f"<h1> {post.title} </h1> <br> <p> {post.content}</p>")


def index(request):
    post = Post.objects.all()
    print(post)
    return render(request,'index.html')


def create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save()
        return HttpResponse(post.title)
    else:
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)


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
