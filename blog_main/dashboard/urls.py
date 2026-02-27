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
   path('users/',views.users,name='users'),
   path('users/add/',views.add_users,name='add_users'),
   path('users/del/<int:user_id>/',views.del_users,name='del_users'),
   path('users/edit/<int:user_id>/',views.edit_users,name='edit_users'),
   
]
