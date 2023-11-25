from django.urls import path
from parse_app.views import get_posts

urlpatterns = [
    path('posts/', get_posts, name='get_posts'),
]
