from blog_app.models import Blog, Category
from django import forms
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
class PostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','Category','featured_image','short_description','blog_body','is_featured','status']