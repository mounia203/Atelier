from django.core.management.base import BaseCommand
from produit.models import Category, Product
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Génère des données factices pour les produits et les catégories'

    def handle(self, *args, **kwargs):
        fake = Faker()

       
        categories = []
        for _ in range(5):
            category = Category.objects.create(
                name=fake.word(),
                slug=fake.slug()
            )
            categories.append(category)

        
        for _ in range(20):
            Product.objects.create(
                name=fake.word(),
                description=fake.text(),
                price=round(random.uniform(10.0, 100.0), 2),
                stock=random.randint(1, 100),
                category=random.choice(categories)
            )

        self.stdout.write(self.style.SUCCESS('Données factices générées avec succès!'))