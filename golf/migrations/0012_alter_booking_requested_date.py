# Generated by Django 4.1.3 on 2022-11-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0011_alter_booking_options_booking_requested_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='requested_date',
            field=models.DateField(default='datetime.now'),
        ),
    ]