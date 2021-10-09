from django.db import models

from multiselectfield import MultiSelectField


class Category(models.Model):
    """ Category model """

    name = models.CharField(max_length=255,
                            verbose_name="Ім'я категорії")
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Категорії'
        verbose_name = "Категорію"

    def __str__(self):
        return self.name


class Brand(models.Model):
    """ Brand model """

    name = models.CharField(max_length=255, verbose_name="Назва")
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Бренди'
        verbose_name = "Бренд"

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Template of product model """

    MIN_RESOLUTION = (200, 200)
    MAX_RESOLUTION = (700, 700)

    class Meta:
        abstract = True

    name = models.CharField(max_length=255, verbose_name="Назва")
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name="Ціна")
    discount_price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name="Знижка", blank=True, null=True)
    description = models.TextField(blank=True, verbose_name="Опис")
    image = models.ImageField(upload_to='products', verbose_name='Зображення')
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, verbose_name='Бренд', null=True)

    in_stock = models.BooleanField(default=True, verbose_name="В наявності")
    is_active = models.BooleanField(default=True, verbose_name="Активне")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.name


class ShoesProduct(Product):
    """ Shoes product model """

    SHOES_SIZE = [
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
    ]

    available_size = MultiSelectField(
        max_length=12, max_choices=5, choices=SHOES_SIZE, verbose_name="Розміра в наявності")
    category = models.ForeignKey(
        Category, related_name='shoes_product', on_delete=models.CASCADE, verbose_name="Категорія")

    class Meta:
        verbose_name_plural = 'Взуття'
        verbose_name = "Продукт - Взуття"


class ClothesProduct(Product):
    """ Clothes product model """

    CLOTHER_SIZE = [
        ('XXL', 'XXL'),
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S'),
    ]

    available_size = MultiSelectField(
        max_length=12, max_choices=5, choices=CLOTHER_SIZE, verbose_name="Розміра в наявності")
    category = models.ForeignKey(
        Category, related_name='clothes_product', on_delete=models.CASCADE, verbose_name="Категорія")

    class Meta:
        verbose_name_plural = 'Одяг'
        verbose_name = "Продукт - Одяг"


class BagProduct(Product):
    """ Bag product model """

    size = models.CharField(
        max_length=155, verbose_name="Розмір", default='Один розмір')
    category = models.ForeignKey(
        Category, related_name='bag_product', on_delete=models.CASCADE, verbose_name="Категорія")

    class Meta:
        verbose_name_plural = 'Рюкзаки'
        verbose_name = "Продукт - Рюкзаки"


class AccessoriesProduct(Product):
    """ Accessories product model """

    size = models.CharField(
        max_length=155, verbose_name="Розмір", default='Один розмір')
    category = models.ForeignKey(
        Category, related_name='accessories_product', on_delete=models.CASCADE, verbose_name="Категорія")

    class Meta:
        verbose_name_plural = 'Аксесуари'
        verbose_name = "Продукт - Аксесуари"
