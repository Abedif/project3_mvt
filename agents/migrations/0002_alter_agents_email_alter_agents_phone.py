# Generated by Django 5.0.6 on 2024-06-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='email',
            field=models.EmailField(default='#', max_length=254),
        ),
        migrations.AlterField(
            model_name='agents',
            name='phone',
            field=models.CharField(default=0, max_length=110),
        ),
    ]