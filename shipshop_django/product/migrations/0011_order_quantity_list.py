# Generated by Django 2.2.4 on 2019-08-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20190814_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity_list',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
