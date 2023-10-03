from django.urls import path

from .views import OrderCreate

urlpatterns = [path('make_order/', OrderCreate.as_view(), name='order')]
