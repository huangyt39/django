from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog_index, name='index'),
    url(r'^cat', views.categorys, name='categorys'),
    url(r'^(?P<article_id>[0-9]+)/', views.article,name='artcile'),
    url(r'^cat=(?P<category_id>[0-9]+)',views.category,name='category')
]