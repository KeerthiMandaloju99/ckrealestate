# Generated by Django 4.0 on 2024-04-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('Event_ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.CharField(max_length=255)),
                ('Event_Desc', models.TextField()),
                ('Event_Image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Event_Address', models.TextField()),
                ('Activity_type', models.CharField(max_length=50)),
            ],
        ),
    ]
