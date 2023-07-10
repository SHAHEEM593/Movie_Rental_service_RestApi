from django.utils import timezone
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=100,
        min_length=8,
        error_messages={
            'required': 'The title field is required.',
            'min_length': 'The title must have a minimum of 2 characters.',
            'max_length': 'The title can have a maximum of 100 characters.',
        }
    )
    release_date = serializers.DateField(
        error_messages={
            'required': 'The release date field is required.',
            'invalid': 'Invalid release date format.',
        }
    )
    genre = serializers.ChoiceField(
        choices=["Action", "Drama", "Comedy", "Thriller", "Sci-Fi"],
        error_messages={
            'required': 'The genre field is required.',
            'invalid_choice': 'Invalid genre choice.',
        }
    )
    duration_minutes = serializers.IntegerField(
        min_value=1,
        max_value=600,
        error_messages={
            'required': 'The duration minutes field is required.',
            'min_value': 'The duration must be at least 1 minute.',
            'max_value': 'The duration cannot exceed 600 minutes (10 hours).',
        }
    )
    rating = serializers.FloatField(
        min_value=0.0,
        max_value=10.0,
        required=False,
        error_messages={
            'min_value': 'The rating must be between 0.0 and 10.0.',
            'max_value': 'The rating must be between 0.0 and 10.0.',
            'invalid': 'Invalid rating value.',
        }
    )

    def validate_title(self, value):
        if not value.startswith('Movie-'):
            raise serializers.ValidationError('Title must start with "Movie-".')
        return value

    def validate_release_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError('Release date cannot be in the future.')
        if value < timezone.now().date() - timezone.timedelta(days=30 * 365):
            raise serializers.ValidationError('Release date should be within the last 30 years.')
        return value

    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'genre', 'duration_minutes', 'rating']
