import re
from datetime import datetime

from django.core.exceptions import ValidationError


def validate_model_version(value):
    """Валидатор версии и модели."""
    pattern = r"^[a-zA-Z0-9]*$"
    if re.match(pattern, value):
        return value
    raise ValidationError(
        "Некорректное название модели или версии, название должно "
        "состоять из цифр или английских букв."
    )


def validate_past_datetime(value):
    """Валидатор для проверки даты и времени."""
    current_time = datetime.now().replace(tzinfo=None)
    if value.replace(tzinfo=None) >= current_time:
        raise ValidationError(
            "Дата создания не может быть позже текущего времени."
        )
