from blog_app.models import Blog, Category
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
class PostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','Category','featured_image','short_description','blog_body','is_featured','status']
class Userform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','is_staff','is_active','groups','user_permissions'] 
class edituserform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','is_staff','is_active','groups','user_permissions']
