# Generated by Django 4.1.7 on 2023-04-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0007_retainerinvoice_terms_and_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retainerinvoice',
            name='total_amount',
            field=models.CharField(max_length=100),
        ),
    ]
