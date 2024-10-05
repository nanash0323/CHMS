# Generated by Django 4.2.5 on 2023-10-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_room_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('room_type', models.CharField(max_length=50)),
                ('num_beds', models.IntegerField()),
                ('bed_type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='rooms',
        ),
    ]
