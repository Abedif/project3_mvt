# Generated by Django 5.0.6 on 2024-06-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_alter_agents_email_alter_agents_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]