# Generated by Django 3.2.11 on 2022-01-25 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_activity_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomGiphy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(default='https://media.giphy.com/media/NENOgw8mgH0NW/giphy.gif')),
            ],
        ),
    ]
