# Generated by Django 3.1.6 on 2021-02-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Ваша почта')),
                ('phone', models.IntegerField(null=True, verbose_name='Ваш номер +7')),
            ],
        ),
    ]
