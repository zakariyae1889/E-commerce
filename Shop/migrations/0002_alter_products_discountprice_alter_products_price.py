# Generated by Django 4.2.4 on 2023-09-01 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='DiscountPrice',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='Price',
            field=models.PositiveIntegerField(),
        ),
    ]
