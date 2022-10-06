from re import template
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('show/<selectedCat>',views.show,name='show'),
    path('addProduct/<selectedCatId>',views.addProduct,name='addProduct'),
    path('addData/',views.addData,name='addData'),
    path('edit/<pk>',views.edit,name='edit'),
    path('update',views.update,name='update'),
    path('delete/<pk>',views.delete,name='delete'),
    path('login/',auth_views.LoginView.as_view(template_name='list/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='list/logout.html'),name='logout'),
    path('register/',views.register,name='register'),
    path('homeUser/',views.showUserHome,name='homeUser'),
    path('categories/',views.showCategories,name='categories'),
    path('addToCart/<productId>/<userId>',views.addToCart,name='addToCart'),
    path('viewCart/<userId>',views.showCart,name='viewCart'),
    path('viewProductDetails/<productId>',views.viewProductDetails,name='viewProductDetails'),
    path('viewOffer',views.showOffers,name='viewOffer'),
    path('deleteFromCart/<userId>/<productId>',views.deleteFromCart,name='deleteFromCart',)
]

