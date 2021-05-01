from django.urls import path

from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
app_name = 'blogs'
urlpatterns = [
  path('', BlogListView.as_view(), name='blogs'),
  path('post/', BlogCreateView.as_view(), name="blog-post"),
  path('<int:pk>/', BlogDetailView.as_view(), name="blog"),
  #path('<int:pk>/', BlogDeleteView.as_view(), name="blog")
  #path('<int:pk>/', BlogUpdateView.as_view())
]