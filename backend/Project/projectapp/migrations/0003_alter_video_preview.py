# Generated by Django 4.1.3 on 2022-12-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
