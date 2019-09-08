 
from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from hotels import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hotels/list/', views.HotelsList.as_view(), name="hotels-list"),
    path('hotels/details/<int:hotel_id>/', views.HotelDetails.as_view(), name="hotel-details"),
    path('hotels/book/<int:hotel_id>/', views.BookHotel.as_view(), name="book-hotel"),

    path('bookings/', views.BookingsList.as_view(), name="bookings-list"),
    path('bookings/cancel/<int:booking_id>/', views.CancelBooking.as_view(), name="cancel-booking"),
    path('bookings/modify/<int:booking_id>/', views.ModifyBooking.as_view(), name="modify-booking"),

    path('profile/', views.Profile.as_view(), name="profile"),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/',  views.Register.as_view() , name="register"),
]
