# Generated by Django 5.0.2 on 2024-02-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_docters_booking_field_alter_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docters_booking',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='docters_booking',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
