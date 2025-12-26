from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.models import User
from apps.bookings.models import Booking
from common.permissions import IsOpsManager
from .models import CollectorProfile

from rest_framework.generics import ListAPIView
from apps.bookings.serializers import BookingListSerializer

from django.db.models import Q

class CreateCollectorView(APIView):
    permission_classes = [IsAuthenticated, IsOpsManager]
    

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        vehicle_number = request.data["vehicle_number"]
        service_area = request.data["service_area"]

        collector = User.objects.create_user(
            email=email,
            password=password,
            role=User.Role.COLLECTOR,
        )

        CollectorProfile.objects.create(
            user=collector,
            vehicle_number=vehicle_number,
            service_area=service_area,
        )

        return Response(
            {"message": "Collector created"},
            status=status.HTTP_201_CREATED,
        )


class AssignCollectorView(APIView):
    permission_classes = [IsAuthenticated, IsOpsManager]

    def post(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        collector_id = request.data["collector_id"]

        collector = User.objects.get(
            id=collector_id,
            role=User.Role.COLLECTOR,
        )

        booking.assigned_collector = collector
        booking.status = Booking.Status.ASSIGNED
        booking.save()

        return Response({"message": "Collector assigned"})

class OpsUnassignedBookingsView(ListAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated, IsOpsManager]

    def get_queryset(self):
        return Booking.objects.filter(
            status=Booking.Status.CREATED,
            assigned_collector__isnull=True,
        ).order_by("created_at")
    

class OpsAvailableCollectorsView(ListAPIView):
    permission_classes = [IsAuthenticated, IsOpsManager]

    def list(self, request, booking_id):
        booking = Booking.objects.get(id=booking_id)

        booking_area = booking.pickup_address_snapshot.get("area")

        # Step 1: collectors serving the same area & online
        collectors = User.objects.filter(
            role=User.Role.COLLECTOR,
            collector_profile__service_area=booking_area,
            collector_profile__is_online=True,
        )

        # Step 2: exclude busy collectors
        busy_collectors = Booking.objects.filter(
            status__in=[
                Booking.Status.PENDING_COLLECTOR_CONFIRMATION,
                Booking.Status.ASSIGNED,
                Booking.Status.ON_THE_WAY,
                Booking.Status.PICKED_UP,
            ]
        ).values_list("assigned_collector_id", flat=True)

        available_collectors = collectors.exclude(
            id__in=busy_collectors
        )

        data = [
            {
                "collector_id": c.id,
                "email": c.email,
                "service_area": c.collector_profile.service_area,
                "vehicle_number": c.collector_profile.vehicle_number,
            }
            for c in available_collectors
        ]

        return Response(data)