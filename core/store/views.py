from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from collections import namedtuple

from .models import (ShoesProduct, ClothesProduct,
                     BagProduct, AccessoriesProduct)
from .serializers import (ProductListSerializer, ProductDetailSerializer)
from itertools import chain


Products = namedtuple('Products', ('shoes', 'clothes', 'bags', 'accessories'))


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

    def get(self, reqeust, product_slug):
        products = list(chain(ClothesProduct.objects.all(), ShoesProduct.objects.all(),
                              BagProduct.objects.all(), AccessoriesProduct.objects.all()))
        for product in products:
            if product.slug == product_slug:
                product = product

        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
