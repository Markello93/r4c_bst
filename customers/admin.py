from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Админ модель для клиентов."""

    list_display = (
        'id',
        'email',
    )
    search_fields = ('email',)
    list_filter = ('email',)
