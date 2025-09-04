from rest_framework import serializers
from .models import Listing, Review, Booking


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    Converts Listing instances to/from JSON format.
    """
    
    class Meta:
        model = Listing
        fields = [
            'listings_id',
            'host_id', 
            'name',
            'description',
            'location',
            'price_per_night',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['listings_id', 'created_at', 'updated_at']


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    Handles review data conversion and validation.
    """
    
    class Meta:
        model = Review
        fields = [
            'review_id',
            'user_id',
            'property_id',
            'rating',
            'comment',
            'created_at'
        ]
        read_only_fields = ['review_id', 'created_at']
    
    def validate_rating(self, value):
        """
        Custom validation for rating field.
        """
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Handles booking data with date validation.
    """
    
    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'user_id',
            'property_id',
            'start_date',
            'end_date',
            'total_price',
            'created_at'
        ]
        read_only_fields = ['booking_id', 'created_at']
    
    def validate(self, data):
        """
        Custom validation to ensure end_date is after start_date.
        """
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data
