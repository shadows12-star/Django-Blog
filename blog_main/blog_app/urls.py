from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('categories/<int:category_id>/',views.category_posts,name='category_posts'),
   
]
