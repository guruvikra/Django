# Generated by Django 4.2.7 on 2023-11-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newww', '0006_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavRest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_user_name', models.CharField(blank=True, default=None, max_length=100)),
                ('rest_hotel_name', models.CharField(blank=True, default=None, max_length=100)),
            ],
        ),
    ]
