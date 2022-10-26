# Generated by Django 4.0.6 on 2022-10-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manikshop', '0009_extended_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
            ],
        ),
    ]