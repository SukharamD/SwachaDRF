from django.contrib import admin
from .models import Booking, BookingEvent

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "scheduled_time", "created_at")
    list_filter = ("status",)
    search_fields = ("id", "user__email")


@admin.register(BookingEvent)
class BookingEventAdmin(admin.ModelAdmin):
    list_display = ("booking", "event_type", "performed_by", "timestamp")
