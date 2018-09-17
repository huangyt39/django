from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def blog_index(request):
    blog_list = Blog.objects.all()
    return render(request, 'index.html', {'blog_list':blog_list})
