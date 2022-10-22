# Generated by Django 4.0.5 on 2022-10-22 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0002_alter_profile_user_alter_workout_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.date(2022, 10, 22)),
        ),
    ]
