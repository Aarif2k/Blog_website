from typing import Any
from Website.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This commands inserts Category data"

    def handle(self, *args: Any, **options: Any) -> str | None:
        
        categories = ['Sports','Technology','Science','Art','Food']
            
        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        