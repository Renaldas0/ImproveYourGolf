# Generated by Django 4.1.3 on 2022-11-16 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0005_alter_booking_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='ClassName',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
