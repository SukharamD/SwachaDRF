from django.urls import path
from .views import (
    BookingValidateView,
    BookingCreateView,
    BookingListView,
    ActiveBookingView,
    BookingDetailView,
    CancelBookingView,
    BookingTimelineView,
)
from .views import CancelledBookingView


urlpatterns = [
    path("validate/", BookingValidateView.as_view()),
    path("", BookingCreateView.as_view()),
    path("list/", BookingListView.as_view()),
    path("active/", ActiveBookingView.as_view()),
    path("<int:pk>/", BookingDetailView.as_view()),
    path("<int:pk>/cancel/", CancelBookingView.as_view()),
    path("<int:pk>/timeline/", BookingTimelineView.as_view()),
    path("cancelled/", CancelledBookingView.as_view()),
]
