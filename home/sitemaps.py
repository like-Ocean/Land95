from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ProductCategory, Product

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['home:home', 'home:all_categories']

    def location(self, item):
        return reverse(item)

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ProductCategory.objects.all()

    def location(self, obj):
        return reverse('home:category_products', args=[obj.slug])

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return reverse('home:product_detail', args=[obj.slug])
