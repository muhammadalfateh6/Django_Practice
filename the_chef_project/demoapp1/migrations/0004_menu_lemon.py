# Generated by Django 5.0.2 on 2024-03-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp1', '0003_alter_customer_table_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu_lemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
