from django.contrib import admin
from .models import CollectorProfile, CollectorLocation


@admin.register(CollectorProfile)
class CollectorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "vehicle_number",
        "service_area",
        "is_online",
    )

    list_filter = (
        "is_online",
        "service_area",
    )

    fields = (
        "user",
        "vehicle_number",
        "service_area",
        "is_online",
    )


@admin.register(CollectorLocation)
class CollectorLocationAdmin(admin.ModelAdmin):
    list_display = ("collector", "booking", "updated_at")
