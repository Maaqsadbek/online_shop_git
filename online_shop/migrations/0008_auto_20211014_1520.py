# Generated by Django 3.2.7 on 2021-10-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0007_onemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arizalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('fam', models.CharField(max_length=50)),
                ('adres', models.CharField(max_length=200)),
                ('ish_joy', models.CharField(max_length=200)),
                ('telefon_raqam', models.IntegerField()),
                ('maxsulot_nomi', models.CharField(max_length=800)),
                ('soni', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='onemail',
            name='nomi',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]