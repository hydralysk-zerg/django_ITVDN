# Generated by Django 4.0.4 on 2022-04-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='discount_size',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=5),
        ),
    ]
