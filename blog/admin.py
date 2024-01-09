from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    This is admin panem view for post.
    This is to tell admin panel where we want to use summernote.
    In models.py class Post, content section.
    """
    list_display = ('title', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content', ]
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This is admin panel view for comment.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body' ]
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)