# Generated by Django 3.1.7 on 2021-03-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountpln',
            name='transaction_type',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
