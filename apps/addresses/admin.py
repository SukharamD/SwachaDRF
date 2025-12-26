from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "city",
        "pincode",
        "address_type",
        "is_default",
    )
    list_filter = ("city", "address_type", "is_default")
