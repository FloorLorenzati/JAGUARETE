# Generated by Django 3.2.4 on 2021-07-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0004_auto_20210615_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='producto_precio',
            field=models.IntegerField(default=0),
        ),
    ]
