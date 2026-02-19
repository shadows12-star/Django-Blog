from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('categories/<int:category_id>/',views.category_posts,name='category_posts'),
    
    path('details/<slug:slug>/',views.blog_details,name='blog_details'),
    path('search/',views.search,name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
   
   
]
