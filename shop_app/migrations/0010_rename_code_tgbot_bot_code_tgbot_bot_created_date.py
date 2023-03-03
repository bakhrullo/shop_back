# Generated by Django 4.1.4 on 2022-12-29 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0009_tgbot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tgbot',
            old_name='code',
            new_name='bot_code',
        ),
        migrations.AddField(
            model_name='tgbot',
            name='bot_created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]