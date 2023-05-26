from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','created','user')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id','post')

admin.site.register(Post, PostsAdmin)
admin.site.register(Comment, CommentsAdmin)

