# Generated by Django 5.0.2 on 2024-03-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_table',
            name='Time',
            field=models.TimeField(null=True),
        ),
    ]
