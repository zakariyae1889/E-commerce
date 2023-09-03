# Generated by Django 4.2.2 on 2023-09-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_rename_name_reviews_name_remove_reviews_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='color',
        ),
        migrations.RemoveField(
            model_name='products',
            name='size',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue'), ('Green', 'Green')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(choices=[('XS', 'xs'), ('S', 's'), ('M', 'm'), ('L', 'l'), ('XL', 'xl'), ('XXL', 'xxl')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
