from ast import keyword
from itertools import count
from django.shortcuts import get_object_or_404, redirect, render
from . models import Blog,Category
from django.db.models import Q
from . forms import RegistrationForm,CommentForm
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  
    featured_posts=Blog.objects.filter(is_featured=True).order_by('updated_at')[:5]
    posts=Blog.objects.filter(is_featured=False).order_by('updated_at')[:10]
    context={
     
        'featured_posts':featured_posts,
        'posts':posts
    }
    return render(request,'home.html',context)
def category_posts(request,category_id):
   
    featured_posts=Blog.objects.filter(Category__id=category_id,status='published',is_featured=True).order_by('-created_at')

    categoryname=get_object_or_404(Category,id=category_id).name
    
    context={
        'featured_posts':featured_posts,
     
        'categoryname':categoryname
    }
    return render(request,'categories.html',context)

def blog_details(request,slug):
    form=CommentForm()
    blog=get_object_or_404(Blog,slug=slug)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            
            f1=form.save(commit=False)
            f1.post=blog
            f1.user=request.user
            f1.save()
           
            return redirect('blog_details',slug=slug)
    
    comments=blog.comments_set.all().order_by('-created_at')[:3]
    count=blog.comments_set.all().count()
    context={
        'blog':blog,
        'comments':comments,
        'form':form,
        'count':count
    }
    return render(request,'blog_details.html',context)

def search(request):
    keyword = request.GET.get('keyword')

    posts = Blog.objects.none()
 
    if keyword:
        posts = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status='published'
        ).order_by('-created_at')

    context = {
        'posts': posts,
        'keyword': keyword
    }

    return render(request, 'search.html', context)
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
       
    else:
       form=RegistrationForm()
       context={
        'form':form
        }
    return render(request,'register.html',context)
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('home')
    
    else:
        form=AuthenticationForm()
         
    return render(request,'login.html',context={'form':form})
def logout(request):
    
    auth_logout(request)
    return redirect('dashboard')