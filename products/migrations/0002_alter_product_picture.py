# Generated by Django 5.1.2 on 2024-11-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='imagen'),
        ),
    ]
