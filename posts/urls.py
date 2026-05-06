from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('<int:id>/edit/', views.edit_post, name='edit_post'),
    path('<int:id>/delete/', views.delete_post, name='delete_post'),
]
