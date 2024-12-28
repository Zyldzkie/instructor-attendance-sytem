# Generated by Django 5.0.3 on 2024-04-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_comlab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('In', 'In'), ('Out', 'Out'), ('On Class', 'On Class'), ('On Break', 'On Break'), ('On Leave', 'On Leave'), ('Absent', 'Absent')], default='', max_length=20)),
            ],
        ),
    ]