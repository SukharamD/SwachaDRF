from django.urls import path
from .views import (
    CollectorMyBookingsView,
    CollectorLocationUpdateView,
)

urlpatterns = [
    path("me/bookings/", CollectorMyBookingsView.as_view()),
    path("location/", CollectorLocationUpdateView.as_view()),
]
