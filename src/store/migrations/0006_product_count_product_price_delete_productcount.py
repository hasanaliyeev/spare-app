# Generated by Django 4.1.3 on 2022-11-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_productout_productin_productcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductCount',
        ),
    ]
