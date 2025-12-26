from common.permissions import (
    IsCustomer,
    IsBookingOwner,
    CanCancelBooking,
)

from common.permissions import IsCustomer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Booking, BookingEvent
from .serializers import (
    BookingCreateSerializer,
    BookingListSerializer,
    BookingEventSerializer,
)

class BookingValidateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Placeholder validation logic (expand later)
        return Response({"valid": True})


class BookingCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def post(self, request):
        serializer = BookingCreateSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        return Response(
            BookingListSerializer(booking).data,
            status=status.HTTP_201_CREATED
        )


class BookingListView(ListAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class ActiveBookingView(ListAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user,
            status__in=[
                Booking.Status.CREATED,
                Booking.Status.PENDING_COLLECTOR_CONFIRMATION,
                Booking.Status.ASSIGNED,
                Booking.Status.ON_THE_WAY,
                Booking.Status.PICKED_UP,
            ]
        ).order_by("-created_at")


class BookingDetailView(RetrieveAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated, IsCustomer, IsBookingOwner]

    queryset = Booking.objects.all()


class CancelBookingView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer, CanCancelBooking]

    def patch(self, request, pk):
        booking = Booking.objects.get(pk=pk, user=request.user)

        if booking.status != Booking.Status.CREATED:
            return Response(
                {"error": "Booking cannot be cancelled now"},
                status=status.HTTP_409_CONFLICT
            )

        booking.status = Booking.Status.CANCELLED
        booking.cancel_reason = request.data.get("reason", "")
        booking.save()

        BookingEvent.objects.create(
            booking=booking,
            event_type="BOOKING_CANCELLED",
            performed_by=request.user,
        )

        return Response({"message": "Booking cancelled"})


class BookingTimelineView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer, IsBookingOwner]

    def get(self, request, pk):
        booking = Booking.objects.get(pk=pk, user=request.user)
        events = booking.events.all().order_by("timestamp")
        serializer = BookingEventSerializer(events, many=True)
        return Response(serializer.data)


class CancelledBookingView(ListAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user,
            status=Booking.Status.CANCELLED,
        )
