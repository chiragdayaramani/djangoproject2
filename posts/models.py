import datetime
from posts.managers import CategoryManager, PostManager
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import os
from django.conf import settings

# Create your models here.
class Category(models.Model):

    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(default='',editable=False,max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True,blank=True)

    objects=CategoryManager()

    def save(self,*args,**kwargs):
        value=slugify(self.name)
        self.slug=value
        super().save(*args,**kwargs)

    class Meta:
        verbose_name_plural ="Categories"

    def __str__(self) -> str:
        return self.name

    

class Post(models.Model):


    def generate_cover_pic_path(self,filename):

        if filename != settings.DEFAULT_PIC:    
            base_filename,file_extension=os.path.splitext(filename)
            current_timestamp=datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            filename=(f'{base_filename}_{current_timestamp}{file_extension}')
            return f'post_pics/{filename}'


    title = models.CharField(max_length=250, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(default='', editable=False, max_length=500)
    cover_pic=models.ImageField(default=settings.DEFAULT_PIC,upload_to=generate_cover_pic_path)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(null=True,blank=True)

    objects=PostManager()

    def save(self, *args, **kwargs):
        value = slugify(self.title)
        self.slug = value
        super().save(*args,**kwargs)

  

