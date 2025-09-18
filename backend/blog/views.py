from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.filter(is_published=True)
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {'form': form})
