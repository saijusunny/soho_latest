# Generated by Django 4.0.2 on 2023-05-23 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0013_alter_additem_interstate_alter_additem_intrastate'),
    ]

    operations = [
        migrations.CreateModel(
            name='banking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('alias', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('acc_type', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('ac_holder', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('ac_no', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('ifsc', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('swift_code', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bnk_name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bnk_branch', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('chq_book', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('chq_print', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('chq_config', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_addr', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_country', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_state', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('mail_pin', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_bnk_det', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_pan_no', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_reg_typ', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_gst_no', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bd_gst_det', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
