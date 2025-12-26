from rest_framework import serializers
from .models import Booking, BookingEvent

class BookingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = [
            "pickup_address_snapshot",
            "waste_type",
            "quantity",
            "scheduled_time",
        ]

    def create(self, validated_data):
        user = self.context["request"].user

        booking = Booking.objects.create(
            user=user,
            status=Booking.Status.CREATED,
            **validated_data
        )

        BookingEvent.objects.create(
            booking=booking,
            event_type="BOOKING_CREATED",
            performed_by=user,
        )

        return booking


class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"


class BookingEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingEvent
        fields = "__all__"
