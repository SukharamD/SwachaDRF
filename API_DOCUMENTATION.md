# SWACCHA BACKEND – API DOCUMENTATION

Base URL (Local):
http://127.0.0.1:8000/api/v1/

---

## AUTHENTICATION

1. Register (Customer)
   POST /auth/register/

Request:
{
"email": "user@test.com",
"password": "user@123"
}

Response:
{
"id": 1,
"email": "user@test.com",
"role": "CUSTOMER"
}

---

2. Login (All roles)
   POST /auth/login/

Request:
{
"email": "user@test.com",
"password": "user@123"
}

Response:
{
"access": "<jwt_access_token>",
"refresh": "<jwt_refresh_token>"
}

---

3. Current User (Me)
   GET /auth/me/

Headers:
Authorization: Bearer <access_token>

---

## CUSTOMER – BOOKINGS

4. Create Booking
   POST /bookings/

Headers:
Authorization: Bearer <access_token>

Request:
{
"pickup_address_snapshot": {
"house_or_flat": "12B",
"street": "MG Road",
"area": "Indiranagar",
"city": "Bangalore",
"state": "Karnataka",
"pincode": "560038"
},
"waste_type": "DRY",
"quantity": "MEDIUM",
"scheduled_time": "2025-01-10T10:00:00"
}

---

5. List All Bookings
   GET /bookings/list/

---

6. Active Bookings
   GET /bookings/active/

Active statuses:

- PENDING_COLLECTOR_CONFIRMATION
- ASSIGNED
- ON_THE_WAY
- PICKED_UP

---

7. Cancel Booking
   PATCH /bookings/{booking_id}/cancel/

---

8. Cancelled Bookings
   GET /bookings/cancelled/

---

## OPS MANAGER – OPERATIONS

9. Unassigned Bookings (FIFO)
   GET /ops/bookings/unassigned/

Conditions:

- status = CREATED
- assigned_collector = NULL
- Ordered by created_at ASC

---

10. Available Collectors for Booking
    GET /ops/bookings/{booking_id}/available-collectors/

Filters:

- Role = COLLECTOR
- Same service area
- is_online = True
- Not currently busy

---

11. Assign Collector to Booking
    POST /ops/bookings/{booking_id}/assign/

Request:
{
"collector_id": 5
}

Effect:

- status → PENDING_COLLECTOR_CONFIRMATION

---

## COLLECTOR – BOOKINGS

12. My Assigned Bookings
    GET /collector/bookings/

---

13. Accept Booking (Planned)
    POST /collector/bookings/{booking_id}/accept/

---

14. Reject Booking (Planned)
    POST /collector/bookings/{booking_id}/reject/

---

## AUTHORIZATION RULES

CUSTOMER:

- Can access own bookings only

OPS_MANAGER:

- Can view and assign bookings
- Can view collectors

COLLECTOR:

- Can view own assigned bookings only

---

## NOTES

- All protected APIs require JWT access token
- SQLite used for development
- Production deployment requires DEBUG=False and proper ALLOWED_HOSTS
