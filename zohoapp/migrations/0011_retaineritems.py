# Generated by Django 4.1.7 on 2023-05-03 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0010_remove_retainerinvoice_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retaineritems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('amount', models.CharField(max_length=100)),
                ('retainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.retainerinvoice')),
            ],
        ),
    ]
