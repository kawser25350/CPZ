from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm,ChangeUserForm
from posts.models import Post

# Create your views here.
def profile_view(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Changed.")
            return redirect('author:profile')
    else:
        form = ChangeUserForm(instance=request.user)
    return render(request, 'pages/profile.html', {'form': form})

def passchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Password Change successfull")
            update_session_auth_hash(request, user)
            return redirect('author:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pages/login_and_register_form.html', {'form': form, 'type': 'Change Password'})
    


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            usr = form.cleaned_data.get('username')
            pas = form.cleaned_data.get('password')
            user = authenticate(request, username=usr, password=pas)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'pages/login_and_register_form.html', {'form': form, 'type': 'Login'})
        
            

def register(request):
    if request.method == 'POST':
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.warning(request,"please try again.")
    form=RegisterForm()
    return render(request, 'pages/login_and_register_form.html', {'form': form, 'type': 'Register'})
        


def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='author:login')
def my_posts(request):
    post_data = Post.objects.filter(author=request.user)
    return render(request, 'pages/my_posts.html', {'post_data': post_data})





