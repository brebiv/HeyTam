# Generated by Django 3.0.6 on 2020-05-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200514_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='more_link',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]
