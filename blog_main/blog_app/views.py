from ast import keyword
from django.shortcuts import get_object_or_404, render
from . models import Blog,Category
from django.db.models import Q
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
    blog=get_object_or_404(Blog,slug=slug)
    context={
        'blog':blog
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