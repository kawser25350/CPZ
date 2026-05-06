import os
import django
import sys

sys.path.append(r"P:\Projects\Django\CPZ")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CPZ.settings')
django.setup()

from category.models import Category
from posts.models import Post

print("Categories:", [(c.name, c.slug) for c in Category.objects.all()])
print("Posts:", [(p.name, [c.name for c in p.category.all()]) for p in Post.objects.all()])
