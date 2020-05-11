# Generated by Django 3.0.6 on 2020-05-11 15:30

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200511_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(default=None, null=True, upload_to=main.models.product_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=main.models.product_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_file',
            field=models.FileField(default=None, null=True, upload_to=main.models.product_directory_path),
        ),
    ]
