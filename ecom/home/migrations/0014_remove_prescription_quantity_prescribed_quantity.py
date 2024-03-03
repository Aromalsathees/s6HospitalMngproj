# Generated by Django 5.0.2 on 2024-02-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_prescription_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='quantity',
        ),
        migrations.AddField(
            model_name='prescribed',
            name='quantity',
            field=models.CharField(default='', max_length=100),
        ),
    ]