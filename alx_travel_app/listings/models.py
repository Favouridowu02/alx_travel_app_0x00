import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# Create your models here.

class Listing(models.Model):
    """
    Represents a listing in the travel app.
    """
    listings_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    # host_id = models.ForeignKey('alx_travel_app.User', on_delete=models.CASCADE, null=False, related_name='host_listings')
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    """
    Represents a review for a listing.
    """
    # user_id = models.ForeignKey('alx_travel_app.User', on_delete=models.CASCADE, null=False)
    review_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    property_id = models.ForeignKey('listings.Listing', on_delete=models.CASCADE, null=False)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    """
    Represents a booking for a listing.
    """
    booking_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    # user_id = models.ForeignKey('alx_travel_app.User', on_delete=models.CASCADE, null=False)
    property_id = models.ForeignKey('listings.Listing', on_delete=models.CASCADE, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)