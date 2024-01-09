from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    This will render a list of published blog posts 
    ordered by creation date in descending order.
    Display 3 posts per page, and the rendering is based on
    'index.html' templates.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 3
