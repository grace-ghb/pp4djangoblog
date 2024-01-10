from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from .views import Index, TemplateView

urlpatterns = [
    # path('', Index.as_view(), name='home'),
    # We add as_view() because we use class in PostList.
    path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
  
]