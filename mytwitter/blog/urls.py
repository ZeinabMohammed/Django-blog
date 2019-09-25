from django.contrib import admin
from django.urls import path, include
from .views import *
app_name="blog"

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='about'),
    # path('post/<pk>/comment', add_comment,name='add_acomment'),
    path('post/comment/done', comment_posted ,name='comment_posted'),
    
   
]