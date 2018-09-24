from django.contrib import admin
from blog.models import Blog, Tag, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'timestamp']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Category)