from django.contrib import admin

from .models import Category,Blog
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author','Category','is_featured','status','created_at')
    search_fields = ('title','author__username','Category__name','status')
    list_editable = ('is_featured','status')
     
    

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)