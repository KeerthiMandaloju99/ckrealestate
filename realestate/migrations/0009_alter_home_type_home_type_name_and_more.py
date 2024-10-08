# Generated by Django 4.0 on 2024-05-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0008_pricerange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_type',
            name='Home_Type_Name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='Neighborhood_Name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='Bath',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='Beds',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='Listing_Name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
