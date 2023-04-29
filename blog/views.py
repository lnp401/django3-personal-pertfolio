from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    #blogs = Blog.objects.order_by('-date')                           # вначале отображает свежие блоги
    blogs = Blog.objects.order_by('-date') [:5]                       # отображает не более 5 блогов на страницу
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
    
def detail(request, blog_id): 
    blog = get_object_or_404(Blog, pk=blog_id)   
    return render(request, 'blog/detail.html', {'blog':blog})