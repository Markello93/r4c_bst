from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админ модель для заказов."""

    list_display = ('id', 'customer', 'robot_serial', 'status')
    search_fields = ('customer', 'robot_serial', 'status')
    list_filter = ('customer',)
