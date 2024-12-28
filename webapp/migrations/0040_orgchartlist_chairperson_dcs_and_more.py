# Generated by Django 5.1 on 2024-11-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0039_remove_orgchartlist_orgname_orgchartlist_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgchartlist',
            name='Chairperson_DCS',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orgchartlist',
            name='Instructors',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orgchartlist',
            name='Program_Chair_CS',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orgchartlist',
            name='Program_Chair_IT',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orgchartlist',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='orgchartlist',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]