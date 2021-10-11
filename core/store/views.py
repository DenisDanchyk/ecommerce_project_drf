from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from collections import namedtuple

from .models import (ShoesProduct, ClothesProduct,
                     BagProduct, AccessoriesProduct)
from .serializers import (ProductListSerializer, ProductDetailSerializer,
                          SortProductListSerializer)
from itertools import chain


Products = namedtuple('Products', ('shoes', 'clothes', 'bags', 'accessories'))


class ProductsWithDiscountListView(APIView):
    """ List of products that have discount price """

    def get(self, reqeust):
        product_list = list(chain(ClothesProduct.objects.all(), ShoesProduct.objects.all(),
                                  BagProduct.objects.all(), AccessoriesProduct.objects.all()))
        products = []
        for product in product_list:
            if product.discount_price:
                products.append(product)

        serializer = SortProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductListView(viewsets.ViewSet):
    """ Output list of products """

    def list(self, reqeust):
        products = Products(
            clothes=ClothesProduct.objects.all(),
            shoes=ShoesProduct.objects.all(),
            bags=BagProduct.objects.all(),
            accessories=AccessoriesProduct.objects.all(),
        )

        serializer = ProductListSerializer(products)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """ Output product detail """

    # needs fixing

    def get(self, reqeust, product_slug):
        models = [ClothesProduct, ShoesProduct,
                  BagProduct, AccessoriesProduct]
        product = None
        for model in models:
            try:
                product = model.objects.get(slug=product_slug)
                break
            except:
                pass

        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class ProductListByBrand(APIView):
    """ List of products sorted by brand """

    def get(self, request, brand_slug):
        product_list = list(chain(ClothesProduct.objects.all(), ShoesProduct.objects.all(),
                                  BagProduct.objects.all(), AccessoriesProduct.objects.all()))
        products = []
        for product in product_list:
            if str(product.brand).lower() == brand_slug:
                products.append(product)

        serializer = SortProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductListByCategory(APIView):
    """ List of products sorted by category """

    def get(self, request, category_slug):
        product_list = list(chain(ClothesProduct.objects.all(), ShoesProduct.objects.all(),
                                  BagProduct.objects.all(), AccessoriesProduct.objects.all()))
        products = []
        for product in product_list:
            if product.category.slug == category_slug:
                products.append(product)

        serializer = SortProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductListByPrice(APIView):
    """ List of product sorted by price """

    def get(self, request, min_price, max_price):
        product_list = list(chain(ClothesProduct.objects.all(), ShoesProduct.objects.all(),
                                  BagProduct.objects.all(), AccessoriesProduct.objects.all()))
        products = []
        for product in product_list:
            if product.discount_price:
                if product.discount_price >= int(min_price) and product.discount_price <= int(max_price):
                    products.append(product)
            else:
                if product.price >= int(min_price) and product.price <= int(max_price):
                    products.append(product)

        serializer = SortProductListSerializer(products, many=True)
        return Response(serializer.data)
