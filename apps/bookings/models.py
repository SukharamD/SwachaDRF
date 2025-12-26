from django.db import models
from apps.accounts.models import User

class Booking(models.Model):

    class Status(models.TextChoices):
        CREATED = "CREATED"
        PENDING_COLLECTOR_CONFIRMATION = "PENDING_COLLECTOR_CONFIRMATION"
        ASSIGNED = "ASSIGNED"
        ON_THE_WAY = "ON_THE_WAY"
        PICKED_UP = "PICKED_UP"
        COMPLETED = "COMPLETED"
        CANCELLED = "CANCELLED"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    pickup_address_snapshot = models.JSONField()

    waste_type = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)
    scheduled_time = models.DateTimeField()

    assigned_collector = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assigned_bookings"
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.CREATED
    )

    cancel_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.status}"


class BookingEvent(models.Model):
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name="events"
    )
    event_type = models.CharField(max_length=50)
    performed_by = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
