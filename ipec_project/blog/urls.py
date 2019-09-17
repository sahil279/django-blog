from django.contrib import admin
from django.urls import path,include
from .views import PostListView,PostDetailView,PostUpdateView,PostCreateView,PostDeleteView,UserPostListView
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(),name='blog_home'),
    path('user/<str:username>', views.UserPostListView.as_view(),name='user_posts'),
    path('post/<int:pk>/detail',views.PostDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
]
