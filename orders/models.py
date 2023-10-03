from django.db import models

from customers.models import Customer
from R4C import settings


class Order(models.Model):
    """Модель заказов."""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)
    status = models.CharField(
        'Статус заказа',
        choices=settings.ORDER_STATUS,
        default='CREATED',
        max_length=17,
    )
