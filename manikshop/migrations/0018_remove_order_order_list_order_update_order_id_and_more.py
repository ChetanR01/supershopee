# Generated by Django 4.1.4 on 2023-01-27 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manikshop', '0017_remove_order_order_list_order_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='update_order_id',
            field=models.BooleanField(default=True),
        ),
        ]