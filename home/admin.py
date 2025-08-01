from django.contrib import admin
from .models import HomePageContent, SliderImage, WhyChooseCard, ProductCategory, Product, ProductImage

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ("main_title", "sub_title", "phone_number", "email")
    fields = ("main_title", "sub_title", "phone_number", "email")


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(WhyChooseCard)
class WhyChooseCardAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    fields = ("image", "title", "text", "order")
    

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    fields = ("title", "slug", "image", "description")
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price")
    fields = ("category", "title", "slug", "description", "image", "price", "use_cases")
    prepopulated_fields = {"slug": ("title",)}
    

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image")

