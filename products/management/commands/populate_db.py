from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
 
 
class Command(BaseCommand):
    help = 'Populate DB with sample data (categories, tags, products)'
 
    def handle(self, *args, **options):
        self.stdout.write('Populating DB with sample data...')
 
        try:
            call_command('loaddata', 'sample_data.json')
        except Exception as e:
            raise CommandError(f'Failed to load sample data: {e}')
 
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data.'))
