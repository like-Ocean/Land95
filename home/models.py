from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
import os
from django.utils.text import slugify

class HomePageContent(models.Model):
    main_title = models.CharField(max_length=255, verbose_name="Основной заголовок")
    sub_title = models.CharField(max_length=255, verbose_name="Подзаголовок")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Email")
    
    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = "Контент главной страницы"
        verbose_name_plural = "Контент главной страницы"


class SliderImage(models.Model):
    image = models.ImageField(upload_to="slider_images/", verbose_name="Изображение слайдера")
    
    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"


def validate_image_or_svg(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext == '.svg':
        return
    else:
        try:
            get_image_dimensions(file)
        except Exception:
            raise ValidationError("Загрузите корректное изображение. Файл, который вы загрузили, либо не является изображением, либо поврежден.")


class WhyChooseCard(models.Model):
    image = models.FileField(upload_to="cards/", validators=[validate_image_or_svg], verbose_name="Изображение карточки")
    title = models.CharField(max_length=255, verbose_name="Заголовок карточки")
    text = models.TextField(verbose_name="Текст карточки")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карточка «Почему выбирают нас?»"
        verbose_name_plural = "Карточки «Почему выбирают нас?»"
        ordering = ['order']
        

class ProductCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL категории", blank=True)
    image = models.ImageField(upload_to="category_images/", verbose_name="Изображение категории", blank=True, null=True)
    description = models.TextField(verbose_name="Описание категории", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория продукции"
        verbose_name_plural = "Категории продукции"
        
        
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    title = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")
    image = models.ImageField(upload_to="products/", verbose_name="Изображение товара", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    use_cases = models.TextField(
        verbose_name="Отлично подходит для",
        blank=True,
        help_text="Введите варианты использования, каждый на новой строке"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        
        
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="Товар")
    image = models.ImageField(upload_to="product_images/", verbose_name="Изображение товара")

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товара"




