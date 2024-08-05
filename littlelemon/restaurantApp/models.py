from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
def get_hours():
    return tuple((f"{hour:02}:00", f"{hour:02}:00") for hour in range(10, 23))
    
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    date = models.DateField(default= timezone.now)
    time = models.TimeField()

    def __str__(self):
      return self.first_name
  
    @staticmethod
    def get_available_times(date):
        # Define business hours and interval
        business_hours_start = timezone.datetime.strptime("10:00", "%H:%M").time()
        business_hours_end = timezone.datetime.strptime("22:00", "%H:%M").time()
        interval_minutes = 30

        # Get existing bookings for the restaurant on the specified date
        existing_bookings = Booking.objects.filter(date=date).values_list('time', flat=True)

        # Generate list of available times
        available_times = []
        current_time = business_hours_start
        while current_time < business_hours_end:
            if current_time not in existing_bookings:
                available_times.append(current_time)
            current_time = (timezone.datetime.combine(timezone.now(), current_time) + timezone.timedelta(minutes=interval_minutes)).time()
        
        return available_times

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
  
