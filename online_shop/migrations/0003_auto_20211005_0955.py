# Generated by Django 3.2.7 on 2021-10-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0002_auto_20211002_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='maxsulotlar',
            name='new_prise',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maxsulotlar',
            name='old_prise',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
