# Generated by Django 4.2.4 on 2023-10-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbalance',
            name='transaction_history',
            field=models.JSONField(default=list),
        ),
    ]
