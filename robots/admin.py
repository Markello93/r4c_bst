from django.contrib import admin

from robots.models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    """Админ модель для учета роботов."""

    list_display = (
        "id",
        "serial",
        "model",
        "version",
        "created",
    )
    search_fields = ("serial",)
    list_filter = ("serial",)
