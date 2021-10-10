from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view({'get': 'list'})),
    path('product/<slug:product_slug>/', views.ProductDetailView.as_view())
]
