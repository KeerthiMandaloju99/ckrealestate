# Generated by Django 4.0 on 2024-05-07 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0007_alter_propertyimage_property_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('Price_Range_ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price_Range', models.CharField(max_length=255)),
            ],
        ),
    ]
