# Generated by Django 4.0.6 on 2022-10-23 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manikshop', '0005_remove_productdetails_category_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='manikshop.category'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='manikshop.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='souscategories', to='manikshop.category'),
        ),
    ]
