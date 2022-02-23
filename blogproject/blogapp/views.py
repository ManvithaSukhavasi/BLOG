from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from blogapp.models import Profile, BlogPost, Comment
from blogapp.forms import ProfileForm, BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout




# Create your views here.
def index(request):
    return render(request,"blogapp/base.html")


def Profile(request):
    return render(request, "blogapp/profile.html")


def blogs(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    return render(request, "blogapp/blog.html", {'posts':posts})





def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method=="POST":
        form = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "blogapp/editprofile.html", {'alert':alert})
    else:
        form=ProfileForm()
    return render(request, "blogapp/editprofile.html", {'form':form})










@login_required(login_url='/login')
def addblogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "blogapp/addblogs.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "blogapp/addblogs.html", {'form':form})












def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
 
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'blogapp/login.html')  
    return render(request, "blogapp/register.html")






def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'blogapp/blog.html')   
    return render(request, "blogapp/login.html")





def blogscomments(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog=post)
        comment.save()
    return render(request, "blogapp/blog_comments.html", {'post':post, 'comments':comments})



def Logout(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            logout(request, user)
            messages.success(request, "Successfully Logged Out")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'blogapp/blog.html')   
    return render(request, "blogapp/logout.html")









