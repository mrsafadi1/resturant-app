from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
def get_hours():
    return tuple((f"{hour:02}:00", f"{hour:02}:00") for hour in range(10, 23))
    
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField(default= timezone.now)
    reservation_time = models.CharField(max_length = 5, choices=tuple(get_hours()), default= datetime.now().hour)

    class Meta:
        unique_together = ('reservation_date', 'reservation_time')

    def __str__(self):
      return self.first_name

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
  
