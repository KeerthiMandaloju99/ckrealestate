from django.db import models
import decimal
from djmoney.models.fields import MoneyField 

# Create your models here.

class Event(models.Model):
    Event_ID = models.BigAutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='ID')
    Event_Name = models.CharField(max_length=255, null=False, blank=False)
    Event_Desc = models.TextField(null=False, blank=False)
    Event_Image = models.ImageField(upload_to='event_images/',null=True, blank=True)
    Event_Address = models.TextField(null=False, blank=False)
    Activity_type = models.CharField( max_length=50)
    Event_Start_Date = models.DateField(blank=True, null=True)
    Event_End_Date = models.DateField(blank=True, null=True)
    Event_Price = MoneyField(max_digits=5,default=0, decimal_places=2,default_currency='USD')
    def __str__(self) -> str:
    #    return super().__str__()
        return f"{self.Event_Name}"