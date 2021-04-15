from django.shortcuts import render
from blogs import templates
from blogs.models import Blog

# Create your views here.
def home_view(request):
    preview_blog_objects = list(Blog.objects.all())
    preview_blog_context = {
        'bpreviewobjs':preview_blog_objects
    }
    print(request)
    return render(request, 'home.html', preview_blog_context)


