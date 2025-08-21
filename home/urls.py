from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.all_categories, name='all_categories'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('bloglist/',  views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_item, name='blog_item'),
]
