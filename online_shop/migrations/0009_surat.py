# Generated by Django 3.2.7 on 2021-10-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0008_auto_20211014_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surat', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
