from django.contrib import admin

from .models import Category,Blog,About, SocialLinks
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author','Category','is_featured','status','created_at')
    search_fields = ('title','author__username','Category__name','status')
    list_editable = ('is_featured','status')
     
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','id')
    search_fields = ('name',)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=About.objects.count()
        if count==0:
            return True
        return False


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(SocialLinks)