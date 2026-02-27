from django.shortcuts import redirect, render
from jupyterlab_server import slugify
from blog_app.models import Blog,Category
from django.contrib.auth.decorators import login_required
    
from .forms import CategoryForm,PostForm
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.count()
    blog_count=Blog.objects.count()
    context={
        'category_count':category_count,
        'blog_count':blog_count
    }
    return render(request,'dashboard/dashboard.html',context)
@login_required(login_url='login')
def categories(request):
    return render(request,'dashboard/categories.html')
@login_required(login_url='login')
def add_category(request):
    form=CategoryForm()
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    return render(request,'dashboard/add_category.html',{'form':form})
@login_required(login_url='login')
def edit_category(request,category_id):
    category=Category.objects.get(id=category_id)
    form=CategoryForm(instance=category)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    return render(request,'dashboard/edit_category.html',{'form':form})
def del_category(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories')
def posts(request):
    posts=Blog.objects.all()
    context={
        "posts":posts
    }
    return render(request,'dashboard/posts.html',context)
def add_posts(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)+ "-"+str(post.id)
            post.save()
            return redirect('posts')
        
    return render(request,'dashboard/add_posts.html',{'form':form})
def edit_posts(request,post_id):
    post=Blog.objects.get(id=post_id)
    form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)+ "-"+str(post.id)
            post.save()
            return redirect('posts')
    return render(request,'dashboard/edit_posts.html',{'form':form})
def del_posts(request,post_id):
    post=Blog.objects.get(id=post_id)
    post.delete()
    return redirect('posts')