# Generated by Django 4.1.4 on 2022-12-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0007_alter_order_order_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_price',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Сумма'),
        ),
    ]
