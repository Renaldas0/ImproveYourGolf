# Generated by Django 4.1.3 on 2022-11-24 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golf.classname'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golf.customer'),
        ),
    ]
