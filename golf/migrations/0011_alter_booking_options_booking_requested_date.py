# Generated by Django 4.1.3 on 2022-11-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0010_alter_booking_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name_plural': 'Bookings'},
        ),
        migrations.AddField(
            model_name='booking',
            name='requested_date',
            field=models.DateField(default='today'),
        ),
    ]