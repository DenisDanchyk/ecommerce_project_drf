from rest_framework import serializers

from .models import (ShoesProduct, ClothesProduct,
                     BagProduct, AccessoriesProduct)


class ShoesListSerializer(serializers.ModelSerializer):
    """ List of shoes product """

    class Meta:
        model = ShoesProduct
        fields = ('name', 'slug', 'price', 'discount_price', 'image',
                  'description', 'brand', 'in_stock', 'created')


class CLothesListSerializer(serializers.ModelSerializer):
    """ List of clothes product """

    class Meta:
        model = ClothesProduct
        fields = ('name', 'slug', 'price', 'discount_price', 'image',
                  'description', 'brand', 'in_stock', 'created')


class BagsListSerializer(serializers.ModelSerializer):
    """ List of bags product """

    class Meta:
        model = BagProduct
        fields = ('name', 'slug', 'price', 'discount_price', 'image',
                  'description', 'brand', 'in_stock', 'created')


class AccessoriesListSerializer(serializers.ModelSerializer):
    """ List of accessories product """

    class Meta:
        model = AccessoriesProduct
        fields = ('name', 'slug', 'price', 'discount_price', 'image',
                  'description', 'brand', 'in_stock', 'created')


class ProductListSerializer(serializers.Serializer):
    """ List of products """

    shoes = ShoesListSerializer(many=True)
    clothes = CLothesListSerializer(many=True)
    bags = BagsListSerializer(many=True)
    accessories = AccessoriesListSerializer(many=True)


class ProductDetailSerializer(serializers.ModelSerializer):
    """ Product detail """
    
    brand = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ClothesProduct
        fields = ('name', 'slug', 'price', 'discount_price', 'image', 'available_size',
                  'description', 'brand', 'in_stock', 'created')
