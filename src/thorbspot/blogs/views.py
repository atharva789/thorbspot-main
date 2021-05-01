from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Blog
from .forms import BlogPostForm

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

class BlogListView(ListView):
    template_name = 'blogtemplates/blogs.html'
    queryset = Blog.objects.all()

#def blog_view(request):
#    objs = list(Blog.objects.all())
#    blog_context = {
#       'objects':objs
#    }
#    return render(request, "blogtemplates/blogs.html",blog_context)

class BlogCreateView(CreateView):
    template_name = 'blogpost.html'
    form_class = BlogPostForm
    queryset = Blog.objects.all()

class BlogUpdateView(UpdateView):
    template_name = 'blogpost.html'
    form_class = BlogPostForm
    queryset = Blog.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Blog, id=id_)

#def blogpost_view(request):
#    form = BlogPostForm()
#    if request.method == 'POST':
#        form = BlogPostForm(request.POST)
#        if form.is_valid():
#            Blog.objects.create(**form.cleaned_data)
#            return redirect('../')
#        else:
#            print(form.errors)
#    bp_context = {
#        'form':form
#    }
#    return render(request, 'blogpost.html', bp_context)

class BlogDetailView(DetailView):
    template_name = 'blogview.html'
    queryset = Blog.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Blog, id=id_)

class BlogDeleteView(DeleteView):
    template_name = 'blogview.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Blog, id=id_)

    def get_success_url(self):
        return reverse('blogs:blogs')

#def dynamic_blog_url(request, blog_id):
#    nblog = get_object_or_404(Blog, id=blog_id)
#    queryset = Blog.objects.all()
#
#    if request.method == "POST":
#        nblog.delete()
#        return redirect('../')
#    nblog_context = {
#        'blog': nblog,
#        'objects': queryset
#    }
#   return render(request, 'blogview.html', nblog_context)