from django.contrib import admin
from blogapp.models import Profile, BlogPost, Comment
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image','bio','facebook','linkedin','instagram']

admin.site.register(Profile,ProfileAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','content','image','dateTime']

admin.site.register(BlogPost,BlogPostAdmin)


class CommentForm(admin.ModelAdmin):
    list_display = ['user','content','blog','parent_comment','dateTime']

admin.site.register(Comment,CommentForm)
