from django.urls import path

from shop.views import OrderCreate

urlpatterns = [
    path("create/", OrderCreate.as_view()),
]