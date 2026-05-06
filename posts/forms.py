from .models import Post
from django import forms
from django.db import models

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['author']
     