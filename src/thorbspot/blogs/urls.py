from django.urls import path

from .views import blog_view, blogpost_view, dynamic_blog_url
app_name = 'blogs'
urlpatterns = [
  path('', blog_view, name='blogs'),
  path('post/', blogpost_view, name="blog-post"),
  path('<int:blog_id>/', dynamic_blog_url, name="blog")
]