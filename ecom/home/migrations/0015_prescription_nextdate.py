# Generated by Django 5.0.2 on 2024-02-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_prescription_quantity_prescribed_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='nextdate',
            field=models.CharField(default='', max_length=100),
        ),
    ]