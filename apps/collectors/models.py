from django.db import models
from apps.accounts.models import User
from apps.bookings.models import Booking

class CollectorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="collector_profile"
    )

    vehicle_number = models.CharField(max_length=20)
    service_area = models.CharField(max_length=100)

    is_online = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CollectorProfile - {self.user.email}"


class CollectorLocation(models.Model):
    collector = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="locations"
    )
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name="collector_locations"
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Location - {self.collector.email}"
