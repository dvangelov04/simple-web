# Generated by Django 5.0.6 on 2024-07-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_money_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='budget',
            field=models.IntegerField(default=0),
        ),
    ]
