from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('password/', views.passchange, name='passchange'),
    path('logout/', views.logout_user, name='logout'),
    path('posts/', views.my_posts, name='my_posts'),
]
