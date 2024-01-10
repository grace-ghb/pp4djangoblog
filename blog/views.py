from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# from django.http import HttpResponse
from .models import Post
# from . import views
# from django.views.generic import TemplateView


# def Index(request):
#     return HttpResponse("Hello world")


class PostList(generic.ListView):
    """
    This will render a list of published blog posts 
    ordered by creation date in descending order.
    Display 3 posts per page, and the rendering is based on
    'index.html' templates.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginated_by = 3


class PostDetail(View):
    """
    This will render the comments templates.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
             {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
        