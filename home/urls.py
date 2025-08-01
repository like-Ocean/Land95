from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.all_categories, name='all_categories'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
