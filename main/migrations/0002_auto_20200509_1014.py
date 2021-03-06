# Generated by Django 3.0.6 on 2020-05-09 10:14

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=main.models.product_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=main.models.product_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to=main.models.product_directory_path),
        ),
    ]
