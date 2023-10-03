from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse

from orders.models import Order
from R4C import settings

from .models import Robot


@receiver(post_save, sender=Robot)
def notify_robot_availability(sender, instance, created, **kwargs):
    if created:
        orders_with_robot = Order.objects.filter(
            robot_serial=instance.serial, status='NO_ROBOT_IN_STOCK'
        )

        for order in orders_with_robot:
            subject = 'Робот доступен'
            model, version = order.robot_serial.split('-')
            message = f'Добрый день! Недавно вы интересовались нашим роботом модели {model}, версии {version}. Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами. '
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [order.customer.email]
            order.status = 'READY'
            order.save()
            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                return JsonResponse(
                    {
                        'error': f'Ошибка при попытке отправить email с уведомлением {str(e)}'
                    },
                    status=400,
                )
