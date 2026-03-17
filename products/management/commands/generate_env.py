import os

from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = 'Generate a base .env file.'

    def handle(self, *args, **options):
        if os.path.exists('.env'):
            self.stdout.write(self.style.WARNING('.env file already exists.'))
            return

        secret_key = get_random_secret_key()

        with open('.env', 'w') as f:
            f.write(f'SECRET_KEY={secret_key}\n')

        self.stdout.write(self.style.SUCCESS('.env file created.'))