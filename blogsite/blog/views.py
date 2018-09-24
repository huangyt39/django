from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Blog, Category

# Create your views here.
def blog_index(request):
    blog_list = Blog.objects.all()
    category_list = Category.objects.all()
    return render(request, 'index.html', {'blog_list':blog_list, 'category_list':category_list})


def article(request, article_id):
    try:
        article = Blog.objects.get(pk=article_id)
    except Blog.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'article.html', {'article':article})

def category(request, category_id):
    cur_cat = Category.objects.get(pk = category_id)
    articles = Blog.objects.filter(category = cur_cat)	
    return render(request, 'category.html', {'articles': articles})

def categorys(request):
    category_list = Category.objects.all()
    return render(request, 'categorys.html', {'category_list':category_list})