# Generated by Django 4.0.6 on 2022-10-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_booking_index_of_hour_in_work_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
