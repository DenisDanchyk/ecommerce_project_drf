from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductsWithDiscountListView.as_view()),
    path('products/', views.ProductListView.as_view({'get': 'list'})),
    path('product/<slug:product_slug>/', views.ProductDetailView.as_view()),
    path('products/brand/<slug:brand_slug>/', views.ProductListByBrand.as_view()),
    path('products/category/<slug:category_slug>/', views.ProductListByCategory.as_view()),
    path('products/price/<slug:min_price>/<slug:max_price>/', views.ProductListByPrice.as_view())
]
