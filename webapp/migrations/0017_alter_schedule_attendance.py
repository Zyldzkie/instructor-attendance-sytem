# Generated by Django 5.0.3 on 2024-04-12 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_remove_schedule_end_time_remove_schedule_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='attendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.attendance'),
        ),
    ]