# Generated by Django 5.0.6 on 2024-07-15 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='url',
            field=models.URLField(default='https://github.com/aminjon01?tab=repositories'),
        ),
    ]
