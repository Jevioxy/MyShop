# Generated by Django 4.2.2 on 2024-08-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_alter_order_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, editable=False, max_length=254, null=True, verbose_name='Email пользователя'),
        ),
    ]
