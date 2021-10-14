from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartView.as_view()),
    path('add-to-cart/<slug:ct_model>/<slug:product_slug>/', views.AddToCartView.as_view())
]
