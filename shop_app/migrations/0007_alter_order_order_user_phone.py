# Generated by Django 4.1.4 on 2022-12-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0006_alter_order_order_delivery_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_user_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер'),
        ),
    ]
