# Generated by Django 3.0.6 on 2020-05-29 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'produto', 'verbose_name_plural': 'produtos'},
        ),
    ]
