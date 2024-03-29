from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This is blog post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # featured_image = CloudinaryField('image', default='placeholder')
    # excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_likes', blank=True)

    class Meta:
        """
        Class Meta is used to provide additional information about model.
        This is specifying the default ordering for the queryset ordered 
        by the 'created_on' field in descending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        This returns the count of likes associated with the post.
        """
        return self.likes.count()


class Comment(models.Model):
    """
    This is comment post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    # email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Class Meta is used to provide additional information about model.
        This is specifying the default ordering for the queryset ordered 
        by the 'created_on' field in ascending order.
        """
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
