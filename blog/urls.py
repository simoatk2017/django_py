from django.urls import path
from .views import addpost, getposts,\
    detail_posts,greeting

urlpatterns = [
    path('addpost', addpost, name='addpost'),
    path('', getposts, name='blog.posts'),
    path('detail/<int:pk>', detail_posts, name='detail'),
    path('msg/', greeting),
]
