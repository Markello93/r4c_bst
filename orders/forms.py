from django import forms

from customers.models import Customer
from orders.models import Order
from robots.models import Robot
from robots.validators import validate_model_version


class OrderCreateForm(forms.Form):
    """Форма для создания заказа и валидации заказа в базе данных."""

    email = forms.EmailField(max_length=255)
    model = forms.CharField(max_length=2, validators=[validate_model_version])
    version = forms.CharField(
        max_length=2, validators=[validate_model_version]
    )

    def save_order(self):
        email = self.cleaned_data['email']
        model = self.cleaned_data['model']
        version = self.cleaned_data['version']
        serial = f'{model}-{version}'
        customer, created = Customer.objects.get_or_create(email=email)

        robot = Robot.objects.filter(serial=serial, ordered=False).first()

        if robot:
            robot.ordered = True
            robot.save()
            order = Order(customer=customer, robot_serial=serial,
                          status='READY')
            order.save()
        order = Order(customer=customer, robot_serial=serial,
                      status='NO_ROBOT_IN_STOCK')
        order.save()
