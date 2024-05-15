# Generated by Django 5.0.6 on 2024-05-15 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0004_alter_item_item_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='wishlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_in_wishlist', to='wish.wishlist'),
        ),
    ]