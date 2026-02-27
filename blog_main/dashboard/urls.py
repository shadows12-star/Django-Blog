from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   path('',views.dashboard,name='dashboard'),
   path('categories/',views.categories,name='categories'),
   path('add-category/',views.add_category,name='add_category'),
   path('edit-category/<int:category_id>/',views.edit_category,name='edit_category'),
   path('del_category/<int:category_id>/',views.del_category,name='del_category'),
   path('posts/',views.posts,name='posts'),
   path('edit-posts/<int:post_id>/',views.edit_posts,name='edit_posts'),
   path('del-post/<int:post_id>/',views.del_posts,name='del_post'),
   path('add-posts/',views.add_posts,name='add_posts'),
   
]
