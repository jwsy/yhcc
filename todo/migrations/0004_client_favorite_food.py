# Generated by Django 3.2.11 on 2022-02-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_randomgiphy'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='favorite_food',
            field=models.TextField(blank=True),
        ),
    ]
