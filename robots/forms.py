from django import forms

from robots.models import Robot
from robots.validators import validate_model_version, validate_past_datetime


class RobotCreateForm(forms.Form):
    """Форма для валидации создания робота в базе данных."""

    model = forms.CharField(max_length=2, validators=[validate_model_version])
    version = forms.CharField(
        max_length=2, validators=[validate_model_version]
    )
    created = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M:%S"],
        validators=[validate_past_datetime],
    )

    def save_robot(self):
        model = self.cleaned_data["model"]
        version = self.cleaned_data["version"]
        created = self.cleaned_data["created"]
        serial = f"{model}-{version}"
        robot = Robot(
            serial=serial, model=model, version=version, created=created
        )
        robot.save()
