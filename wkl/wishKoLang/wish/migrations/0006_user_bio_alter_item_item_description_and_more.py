# Generated by Django 5.0.6 on 2024-05-15 23:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0005_alter_item_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='Maxine Bading'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_picture_link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='wishlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wish.wishlist'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wish.user'),
        ),
    ]
