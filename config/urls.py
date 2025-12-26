from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/v1/auth/", include("apps.accounts.urls")),
    path("api/v1/user/", include("apps.addresses.urls")),
    path("api/v1/bookings/", include("apps.bookings.urls")),
    path("api/v1/collector/", include("apps.collectors.urls")),
    path("api/v1/ops/", include("apps.collectors.ops_urls")),
    path("api/v1/user/notifications/", include("apps.notifications.urls")),
]
