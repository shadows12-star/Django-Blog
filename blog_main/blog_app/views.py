from django.shortcuts import get_object_or_404, render
from . models import Blog,Category
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