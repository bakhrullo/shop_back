# Generated by Django 4.1.4 on 2022-12-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_alter_tguser_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tguser',
            name='user_phone',
        ),
        migrations.AddField(
            model_name='order',
            name='order_user_phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Номер'),
        ),
    ]
