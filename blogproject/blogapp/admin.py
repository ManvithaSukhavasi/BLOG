from django.contrib import admin
from blogapp.models import Blogs
# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    list_display = ['Image','title','description','date','likes']

admin.site.register(Blogs,BlogsAdmin)
