# Generated by Django 4.0.6 on 2022-10-22 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manikshop', '0002_category_sub_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_cat',
        ),
    ]