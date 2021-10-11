from django.urls import path

from . import views

urlpatterns = [
    path('personal_information/', views.UserPersonalInformation.as_view()),
    path('edit_personal_information/', views.EditPersonalInformation.as_view()),
]
