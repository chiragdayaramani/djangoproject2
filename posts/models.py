from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):

    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(default='',editable=False,max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(null=True,blank=True)

    def save(self,*args,**kwargs):
        value=slugify(self.name)
        self.slug=value
        super().save(*args,**kwargs)

    class Meta:
        verbose_name_plural ="Categories"

    def __str__(self) -> str:
        return self.name

    

class Post(models.Model):

    title = models.CharField(max_length=250, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(default='', editable=False, max_length=500)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs):
        value = slugify(self.title)
        self.slug = value
        super().save(*args,**kwargs)


