from django.db import models

from realestate.models import Home_Type, PriceRange, Neighborhood


class Propery_Search_Log(models.Model):
    Search_Log_Id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Home_Type_Id = models.ForeignKey(Home_Type, null=True, on_delete=models.DO_NOTHING)
    Price_Range_ID = models.ForeignKey(PriceRange, null=True, on_delete=models.DO_NOTHING)
    Neighborhood_ID = models.ForeignKey(Neighborhood, null=True, on_delete=models.DO_NOTHING)
    Visitor_Search_Date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.Search_Log_Id}"
