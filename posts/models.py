from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=150)
    category=models.ManyToManyField(Category)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.category}"
