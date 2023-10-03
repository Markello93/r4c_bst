from django.contrib import admin

from robots.models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    """Админ модель робота."""

    list_display = ('id', 'serial', 'model', 'version', 'created', 'ordered')
    search_fields = ('serial',)
    list_filter = (
        'serial',
        'ordered',
    )
