from django.db import models
from apps.accounts.models import User
from apps.bookings.models import Booking

class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(max_length=100)
    message = models.TextField()

    related_booking = models.ForeignKey(
        Booking,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.email}"
