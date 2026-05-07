from django.db.models import Q
from django.shortcuts import render
from posts.models import Post
from category.models import Category

def home(request):
    cat_data = Category.objects.all()
    selected_category = request.GET.get('category')
    search_query = request.GET.get('q', '').strip()
    
    post_data = Post.objects.all()
    if selected_category:
        post_data = post_data.filter(category__id=selected_category).distinct()
    if search_query:
        post_data = post_data.filter(
            Q(name__icontains=search_query)
            | Q(content__icontains=search_query)
            | Q(author__username__icontains=search_query)
            | Q(author__first_name__icontains=search_query)
            | Q(author__last_name__icontains=search_query)
            | Q(category__name__icontains=search_query)
        ).distinct()
    
    return render(request, 'pages/home.html', {
        'post_data': post_data,
        'cat_data': cat_data,
        'selected_category': selected_category,
        'search_query': search_query,
    })