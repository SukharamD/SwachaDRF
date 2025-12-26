from rest_framework.permissions import BasePermission
from apps.accounts.models import User
from apps.bookings.models import Booking


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.ADMIN
        )


class IsOpsManager(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.OPS_MANAGER
        )


class IsCollector(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.COLLECTOR
        )


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.CUSTOMER
        )


class IsBookingOwner(BasePermission):
    """
    Customer can access only their own booking
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAssignedCollector(BasePermission):
    """
    Collector can access only assigned bookings
    """

    def has_object_permission(self, request, view, obj):
        return obj.assigned_collector == request.user


class CanCancelBooking(BasePermission):
    """
    Only customer & only if status = CREATED
    """

    def has_object_permission(self, request, view, obj):
        return (
            obj.user == request.user
            and obj.status == Booking.Status.CREATED
        )
