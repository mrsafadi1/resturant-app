from django.db import models
from datetime import datetime, timedelta, time
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
    def get_available_times(date, interval_minutes=60):
        # Define business hours and interval
        business_hours_start = time(10, 0)  # 10:00 AM
        business_hours_end = time(22, 0)    # 10:00 PM

        # Ensure date is a datetime.date object
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d").date()
        elif not isinstance(date, datetime):
            date = datetime.combine(date, time.min)

        # Get existing bookings for the restaurant on the specified date
        existing_bookings = Booking.objects.filter(date=date).values_list('time', flat=True)

        # Generate list of available times
        available_times = []
        current_time = business_hours_start
        while current_time < business_hours_end:
            # Check if the current time is in the list of existing bookings
            if current_time not in existing_bookings:
                available_times.append(current_time)
            # Increment the current time by the interval
            next_time = (datetime.combine(date, current_time) + timedelta(minutes=interval_minutes)).time()
            if next_time <= business_hours_end:
                current_time = next_time
            else:
                break

        return available_times

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
  
