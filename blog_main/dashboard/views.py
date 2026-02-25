from django.shortcuts import redirect, render
from blog_app.models import Blog,Category
from django.contrib.auth.decorators import login_required
    
from .forms import CategoryForm
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