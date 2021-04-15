from django.shortcuts import render
from .models import Blog
from .forms import BlogPostForm

def blog_view(request):
    objs = list(Blog.objects.all())
    blog_context = {
        'objects':objs
    }
    return render(request, "blogtemplates/blogs.html",blog_context)

def blogpost_view(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            Blog.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    bp_context = {
        'form':form
    }
    return render(request, 'blogpost.html', bp_context)

def dynamic_blog_url(request, blog_id):
    nblog = Blog.objects.get(id=blog_id)
    objs = list(Blog.objects.all())
    nblog_context = {
        'blog': nblog,
        'objects': objs
    }
    return render(request, 'blogview.html', nblog_context)