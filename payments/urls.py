from django.contrib import admin
from django.urls import path

from .views import index, PaymentCreate, PaymentUpdate, PaymentDelete

urlpatterns = [
    path('', index, name='index'),
    path('payment/create/', PaymentCreate.as_view(), name='create_payment'),
    path('payment/<str:id>/update/', PaymentUpdate.as_view(), name='payment_update_url'),
    path('payment/<str:id>/delete/',PaymentDelete.as_view(), name='payment_delete_url'),
]