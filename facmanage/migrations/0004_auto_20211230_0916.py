# Generated by Django 3.2.8 on 2021-12-30 03:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facmanage', '0003_auto_20211230_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='brand',
            field=models.CharField(default='x', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='facmanage.category'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_of_order',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='order',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(default='y', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier_to_associate_request',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sta', to='facmanage.supplier'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.CharField(default='m%', max_length=7),
        ),
        migrations.AddField(
            model_name='order',
            name='tax_amount',
            field=models.CharField(default='mn', max_length=10),
        ),
        migrations.AddField(
            model_name='products',
            name='supplier_associated',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sup', to='facmanage.supplier'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
