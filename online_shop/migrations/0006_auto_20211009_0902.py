# Generated by Django 3.2.7 on 2021-10-09 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0005_happy_clents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Happy_clents2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=40)),
                ('rasmi', models.ImageField(upload_to='media/')),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Happy_clents3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=40)),
                ('rasmi', models.ImageField(upload_to='media/')),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Happy_clents',
            new_name='Happy_clents1',
        ),
    ]
