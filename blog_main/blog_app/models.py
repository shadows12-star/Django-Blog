from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug= models.SlugField(max_length=200,unique=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    short_description = models.TextField()
    blog_body = models.TextField()
    is_featured = models.BooleanField(default=False)
    status= models.CharField(max_length=20,choices=(('draft','Draft'),('published','Published')),default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title