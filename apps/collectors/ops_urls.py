from django.urls import path
from .views_ops import CreateCollectorView, AssignCollectorView
from .views_ops import OpsUnassignedBookingsView
from .views_ops import OpsAvailableCollectorsView


urlpatterns = [
    path("collectors/", CreateCollectorView.as_view()),
    path("bookings/<int:pk>/assign/", AssignCollectorView.as_view()),
    path("bookings/unassigned/", OpsUnassignedBookingsView.as_view()),
    path("bookings/<int:booking_id>/available-collectors/", OpsAvailableCollectorsView.as_view()),
]
