from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(max_length=200,unique=True,null=True,blank=True)

    def __str__(self):
        return f"{self.name}"