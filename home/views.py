from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import HomePageContent, SliderImage, WhyChooseCard, ProductCategory, Product

def home(request):
    homepage = HomePageContent.objects.first()
    slider_images = SliderImage.objects.all()
    why_choose_cards = WhyChooseCard.objects.all()
    featured_categories = ProductCategory.objects.all()[:3]
    context = {
        "homepage": homepage,
        "slider_images": slider_images,
        "why_choose_cards": why_choose_cards,
        "featured_categories": featured_categories,
    }
    return render(request, "home/home.html", context)


def all_categories(request):
    categories = ProductCategory.objects.all()
    return render(request, "home/all_categories.html", {"categories": categories})


def category_products(request, slug):
    category = get_object_or_404(ProductCategory, slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        "category": category,
        "products": products,
    }
    return render(request, "home/category_products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    slider_images = []
    if product.image:
        slider_images.append(product.image.url)
    for img in product.images.all():
        slider_images.append(img.image.url)
    
    context = {
        "product": product,
        "slider_images": slider_images,
    }
    return render(request, "home/product_detail.html", context)
