from django.core.management.base import BaseCommand
from decimal import Decimal
from datetime import date, timedelta
import random
from listings.models import Listing, Booking, Review


class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        # Simple sample data
        sample_listings = [
            {
                'name': 'Cozy Downtown Apartment',
                'description': 'A beautiful apartment in the heart of the city.',
                'location': 'New York, USA',
                'price_per_night': Decimal('150.00')
            },
            {
                'name': 'Beach House',
                'description': 'Relaxing beach house with ocean view.',
                'location': 'Miami, USA',
                'price_per_night': Decimal('250.00')
            },
            {
                'name': 'Mountain Cabin',
                'description': 'Peaceful cabin in the mountains.',
                'location': 'Denver, USA',
                'price_per_night': Decimal('120.00')
            },
        ]

        # Create listings
        listings = []
        for data in sample_listings:
            listing = Listing.objects.create(**data)
            listings.append(listing)
            self.stdout.write(f'Created listing: {listing.name}')

        # Create sample bookings
        for listing in listings:
            start_date = date.today() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(2, 7))
            nights = (end_date - start_date).days
            
            Booking.objects.create(
                property_id=listing,
                start_date=start_date,
                end_date=end_date,
                total_price=listing.price_per_night * nights
            )
            self.stdout.write(f'Created booking for: {listing.name}')

        # Create sample reviews
        for listing in listings:
            Review.objects.create(
                property_id=listing,
                rating=random.randint(4, 5),
                comment='Great place to stay!'
            )
            self.stdout.write(f'Created review for: {listing.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully seeded database!')
        )
