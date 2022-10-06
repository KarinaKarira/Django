from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about),
    path('create/',views.create,name='create'),
    path('insert',views.insert,name='add'),
    path('edit/<pk>',views.edit,name='edit'),
    path('update',views.update,name='update'),
    path('delete/<pk>',views.delete,name='delete'),
    path('profile/',views.profile,name='profile'),
    path('viewBlogs/',views.showBlogs,name='viewBlogs')
]