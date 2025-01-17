# Generated by Django 5.1.4 on 2025-01-17 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0046_remove_ins_schedule_instructor_ins_schedule_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ins_schedule',
            name='days',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ins_schedule',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.employee', to_field='idNum'),
        ),
        migrations.AlterField(
            model_name='ins_schedule',
            name='time',
            field=models.TimeField(),
        ),
    ]
