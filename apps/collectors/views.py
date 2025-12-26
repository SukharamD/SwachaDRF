from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import CollectorLocation
from apps.bookings.models import Booking

from common.permissions import IsCollector


class CollectorMyBookingsView(APIView):
    permission_classes = [IsAuthenticated, IsCollector]

    def get(self, request):
        bookings = Booking.objects.filter(
            assigned_collector=request.user
        )
        data = [
            {
                "id": b.id,
                "status": b.status,
                "scheduled_time": b.scheduled_time,
            }
            for b in bookings
        ]
        return Response(data)


class CollectorLocationUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsCollector]

    def post(self, request):
        booking_id = request.data.get("booking_id")
        booking = Booking.objects.get(id=booking_id)

        if booking.status != Booking.Status.ON_THE_WAY:
            return Response(
                {"error": "Tracking allowed only when ON_THE_WAY"},
                status=status.HTTP_409_CONFLICT,
            )

        CollectorLocation.objects.create(
            collector=request.user,
            booking=booking,
            latitude=request.data["latitude"],
            longitude=request.data["longitude"],
        )

        return Response({"message": "Location updated"})
