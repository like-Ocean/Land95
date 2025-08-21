from django.contrib import admin
from .models import HomePageContent, SliderImage, WhyChooseCard,\
 ProductCategory, Product, ProductImage, Article, GalleryImage

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


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("alt_text", "image")
    search_fields = ("alt_text",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "publish_date", "slug")
    list_filter = ("category", "publish_date")
    search_fields = ("title", "body")
    filter_horizontal = ("gallery_images",)
    fieldsets = (
        (None, {
            "fields": ("title", "slug", "seo_title", "meta_description", "body", "category")
        }),
        ("Изображения", {
            "fields": ("hero_image", "preview_image", "gallery_images")
        }),
    )