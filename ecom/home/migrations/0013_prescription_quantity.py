# Generated by Django 5.0.2 on 2024-02-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_prescription_prescribed_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='quantity',
            field=models.CharField(default='', max_length=100),
        ),
    ]