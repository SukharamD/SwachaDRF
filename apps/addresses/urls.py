from django.urls import path
from .views import AddressListCreateView

urlpatterns = [
    path("addresses/", AddressListCreateView.as_view(), name="addresses"),
]
