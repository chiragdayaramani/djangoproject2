from posts.models import Category
from django.contrib import admin
from posts.models import Category,Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)

