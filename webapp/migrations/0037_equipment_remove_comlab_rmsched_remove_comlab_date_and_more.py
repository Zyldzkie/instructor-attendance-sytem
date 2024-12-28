# Generated by Django 5.1 on 2024-11-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0036_comlab_cards_comlab_comlab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('equipment', models.CharField(max_length=50)),
                ('RmSched', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='comlab',
            name='RmSched',
        ),
        migrations.RemoveField(
            model_name='comlab',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comlab',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='comlab',
            name='name',
        ),
    ]