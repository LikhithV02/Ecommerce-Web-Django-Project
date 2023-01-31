# Generated by Django 4.1.5 on 2023-01-30 17:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_remove_orders_id_alter_orders_order_no'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orders',
            unique_together={('user', 'Product', 'Customer', 'order_no')},
        ),
    ]