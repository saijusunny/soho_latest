# Generated by Django 4.0.2 on 2023-05-23 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0014_banking'),
    ]

    operations = [
        migrations.AddField(
            model_name='banking',
            name='opening_bal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
