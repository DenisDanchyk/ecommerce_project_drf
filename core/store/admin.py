from django.contrib import admin
from django.forms import ModelChoiceField

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ShoesProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active', 'price']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}

    """
        Permission to select only approprivate category to the class 
    """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(models.Category.objects.filter(slug='vzuttya'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ClothesProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active', 'price']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}

    """
        Permission to select only approprivate category to the class 
    """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(models.Category.objects.filter(slug='odyag'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BagProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active', 'price']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}

    """
        Permission to select only approprivate category to the class 
    """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(models.Category.objects.filter(slug='ryukzaki'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AccessoriesProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active', 'price']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}

    """
        Permission to select only approprivate category to the class 
    """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(models.Category.objects.filter(slug='aksesuari'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(models.ShoesProduct, ShoesProductAdmin)
admin.site.register(models.ClothesProduct, ClothesProductAdmin)
admin.site.register(models.BagProduct, BagProductAdmin)
admin.site.register(models.AccessoriesProduct, AccessoriesProductAdmin)
