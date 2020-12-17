# Generated by Django 3.1.4 on 2020-12-17 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory_shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('available', models.BooleanField(default=False)),
            ],
        ),
    ]
