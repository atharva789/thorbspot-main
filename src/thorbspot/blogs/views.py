from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('../')
        else:
            print(form.errors)
    bp_context = {
        'form':form
    }
    return render(request, 'blogpost.html', bp_context)

def dynamic_blog_url(request, blog_id):
    nblog = get_object_or_404(Blog, id=blog_id)
    queryset = Blog.objects.all()

    if request.method == "POST":
        nblog.delete()
        return redirect('../')
    nblog_context = {
        'blog': nblog,
        'objects': queryset
    }
    return render(request, 'blogview.html', nblog_context)