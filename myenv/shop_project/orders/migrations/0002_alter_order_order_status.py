# Generated by Django 5.0.6 on 2024-10-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(2, 'ORDER_PROCESSED'), (3, 'ORDER_DELERED'), (4, 'ORDER_REJECTED')], default=0),
        ),
    ]