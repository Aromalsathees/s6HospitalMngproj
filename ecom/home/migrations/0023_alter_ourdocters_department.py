# Generated by Django 5.0.2 on 2024-02-24 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_docters_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourdocters',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.deppp'),
        ),
    ]
