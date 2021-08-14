from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: object, **options: object) -> None:
        print(getattr(settings, "MY_EXAMPLE_SETTING", "failfailfail"))
