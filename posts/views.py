from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages
from .models import Post

# Create your views here.
@login_required(login_url='author:login')
def add_post(request):
    if request.method == 'POST':
        form=PostForm(data=request.POST)
        if form.is_valid():
            form.instance.author=request.user
            form.save()
            messages.success(request,"Post Successfully Uploaded!")
            return redirect('posts:add_post')
        messages.error(request,"Please fix the errors below and try again.")
    
    form=PostForm()
    return render(request,'pages/add_post.html',{'form':form,'type':'Post'})

@login_required(login_url='author:login')
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    
    # Check ownership
    if post.author != request.user:
        messages.error(request, "You can only edit your own posts.")
        return redirect('author:my_posts')
    
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post edited Successfully.")
            return redirect('author:my_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'pages/add_post.html', {'form': form, 'type': 'Edit Post'})

@login_required(login_url='author:login')
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    
    # Check ownership
    if post.author != request.user:
        messages.error(request, "You can only delete your own posts.")
        return redirect('author:my_posts')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('author:my_posts')
    
    # GET request: show confirmation page
    return render(request, 'pages/delete_post.html', {'post': post})