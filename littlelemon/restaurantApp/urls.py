from django.urls import path
from .views import *


urlpatterns = [
    path('bookings/', BookingListCreate.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroy.as_view(), name='booking-detail'),
    path('menus/', MenuListCreate.as_view(), name='booking-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroy.as_view(), name='booking-detail'),
]