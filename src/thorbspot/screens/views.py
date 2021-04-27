from django.shortcuts import render
from blogs import templates
from blogs.models import Blog

# Create your views here.
def home_view(request):
    preview_blog_objects = Blog.objects.all()
    preview_blog_context = {
        'blogquery':preview_blog_objects
    }
    return render(request, 'home.html', preview_blog_context)


