# Generated by Django 5.0.2 on 2024-02-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_bloodavailabilty'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourdocters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('department', models.CharField(default='', max_length=100)),
                ('position', models.CharField(default='', max_length=100)),
                ('workingtime', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
