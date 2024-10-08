from django.db import models
import decimal
from djmoney.models.fields import MoneyField

# Create your models here.
# PropertyListing Model

class Neighborhood(models.Model):
    Neighborhood_ID = models.BigAutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='ID')
    Neighborhood_Name = models.CharField(max_length=200, unique=True)
    def __str__(self) -> str:
        return f"{self.Neighborhood_Name}"
    
class Home_Type(models.Model):
    Home_Type_ID = models.BigAutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='ID')
    Home_Type_Name = models.CharField(max_length=100, unique=True)
    def __str__(self) -> str:
        return f"{self.Home_Type_Name}"

class PropertyListing(models.Model):
    Listing_ID = models.BigAutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='ID')
    Listing_Name = models.CharField(max_length=255, unique=True)
    Listing_Desc = models.TextField()
    Listing_Address = models.CharField(max_length=255)
    Beds = models.DecimalField(max_digits=2, decimal_places=0)
    Bath = models.DecimalField(max_digits=3, decimal_places=1)
    Price = MoneyField(max_digits=10,default=0,decimal_places=2,default_currency='USD')
    Is_Featured_Property = models.BooleanField(default=False)
    Is_Visible = models.BooleanField(default=True)
    Availability_Status = models.CharField(max_length=50, default='Available')
    Listing_Neighborhood = models.ForeignKey(Neighborhood, null=True, on_delete=models.CASCADE)
    Listing_Home_Type = models.ForeignKey(Home_Type, null=True, on_delete=models.DO_NOTHING)

    @property
    def get_images(self):
        return self.images.all()
    @property
    def first_image(self):
        return self.images.first()

    def __str__(self) -> str:
        return f"{self.Listing_Name}"

    
class PropertyImage(models.Model):
    Image_ID = models.BigAutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='ID')
    Property_Image = models.ImageField(upload_to='property_images/')
    Property_Listing = models.ForeignKey(PropertyListing, null=True, blank=True, related_name='images',
                                         on_delete=models.CASCADE)
class PriceRange(models.Model):
    Price_Range_ID = models.BigAutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='ID')
    Price_Range = models.CharField(max_length=255)


