from django.shortcuts import render
from posts.models import Post
from category.models import Category

def home(request):
    cat_data = Category.objects.all()
    selected_category = request.GET.get('category')
    
    post_data = Post.objects.all()
    if selected_category:
        post_data = post_data.filter(category__id=selected_category).distinct()
    
    return render(request, 'pages/home.html', {
        'post_data': post_data,
        'cat_data': cat_data,
        'selected_category': selected_category,
    })