from django.urls import path

from . import views

urlpatterns = [
    path('checkout/', views.CheckoutView.as_view()),
    path('create_order/', views.CreateOrderView.as_view())
]
