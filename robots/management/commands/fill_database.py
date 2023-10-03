import random

from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from faker import Faker

from robots.models import Robot


class Command(BaseCommand):
    help = 'Заполнение базы данных тестовыми данными.'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(100):
            model = random.choice(['R2', 'S4', 'F4', 'B8', 'G8', 'I8', 'X6'])
            version = random.choice(['S4', 'H6', '15', '17', 'K8', 'Q8', '19'])
            naive_datetime = fake.date_time_between(
                start_date='-30d', end_date='now', tzinfo=None
            )
            created = make_aware(naive_datetime)
            serial = f'{model}-{version}'
            robot = Robot(
                serial=serial, model=model, version=version, created=created
            )
            robot.save()

        self.stdout.write(
            self.style.SUCCESS(
                'Тестовые данные успешно загружены в базу данных'
            )
        )
