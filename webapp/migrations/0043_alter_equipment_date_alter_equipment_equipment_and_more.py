# Generated by Django 5.1 on 2024-11-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0042_rename_chairperson_dcs_positiondcs_positions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]