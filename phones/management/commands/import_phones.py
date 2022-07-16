import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_record = Phone()
            phone_record.name = phone['name']
            phone_record.price = phone['price']
            phone_record.image = phone['image']
            phone_record.release_date = phone['release_date']
            phone_record.lte_exists = phone['lte_exists']
            phone_record.slug = slugify(phone['name'])
            phone_record.save()

