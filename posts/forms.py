from django import forms
from django.db.models import fields
from .models import Post,Category

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['title','content','category']

class CategoryForm(forms.ModelForm):

    class Meta:
        model=Category
        fields=['name']