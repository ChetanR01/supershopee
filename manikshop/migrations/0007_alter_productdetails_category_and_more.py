# Generated by Django 4.0.6 on 2022-10-23 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manikshop', '0006_productdetails_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='manikshop.category'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='manikshop.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='souscategories', to='manikshop.category'),
        ),
    ]
