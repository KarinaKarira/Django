# Generated by Django 4.0.6 on 2022-09-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0007_cart_product_user_cart_product_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='file',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
