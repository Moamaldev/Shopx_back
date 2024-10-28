# Generated by Django 5.1.1 on 2024-10-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_prouducts_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='prouducts_test',
        ),
        migrations.AddField(
            model_name='order',
            name='products_list',
            field=models.JSONField(default=list),
        ),
    ]
