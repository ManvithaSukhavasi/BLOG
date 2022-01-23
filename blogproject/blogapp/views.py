from django.shortcuts import render,redirect
from blogapp.forms import BlogsForm
from blogapp.models import Blogs
# Create your views here.
def home_view(request):
    AllBlogs = Blogs.objects.all()
    context = {
        'blogs':AllBlogs,
    }
    return render(request,'blogapp/home.html',context)

def addblog_view(request):
    form = BlogsForm()
    if request.method=='POST':
        form = BlogsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home_view)
    context = {
        'form':form,
    }
    return render(request,'blogapp/addblog.html',context)

def likeblog_view(request,pk):
    blog = Blogs.objects.get(id=pk)
    blog.likes+=1
    blog.save()
    return redirect(home_view)