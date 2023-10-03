from django.db import models


class Customer(models.Model):
    """Модель клиента."""

    email = models.EmailField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.email
