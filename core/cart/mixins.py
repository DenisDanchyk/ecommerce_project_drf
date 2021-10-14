from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from django.db import models


class CartMixin(APIView):
    """ Parameters and functions for frequent use """

    def dispatch(self, request, *args, **kwargs):
        ct_model = kwargs.get('ct_model')
        product_slug = kwargs.get('product_slug')
        content_type = ContentType.objects.get(model=ct_model)

        self.content_type = content_type
        self.product_slug = product_slug

        return super().dispatch(request, *args, **kwargs)

    def recalc_cart(self, cart):
        cart_data = cart.products.aggregate(
            models.Sum('final_price'), models.Count('id'))
        if cart_data.get('final_price__sum'):
            cart.final_price = cart_data['final_price__sum']
        else:
            cart.final_price = 0
        cart.total_products = cart_data['id__count']
