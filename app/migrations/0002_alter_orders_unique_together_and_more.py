# Generated by Django 4.1.4 on 2023-01-22 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orders',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='seller',
            name='seller_login_pass',
        ),
        migrations.AddField(
            model_name='cart',
            name='Product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='pr_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_email_id',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='order_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.cart'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='pr_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.product'),
        ),
        migrations.AlterUniqueTogether(
            name='orders',
            unique_together={('user', 'pr_id', 'order_no', 'c_id')},
        ),
    ]