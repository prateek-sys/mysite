from django.contrib import admin

from .models import Post


# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', 'slug', 'summary', 'content', 'published', 'created']


admin.site.register(Post)
