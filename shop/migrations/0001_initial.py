# Generated by Django 5.2.4 on 2025-07-16 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('total_cost', models.IntegerField()),
                ('payment_method', models.CharField(max_length=100)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
    ]
