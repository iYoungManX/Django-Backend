# Generated by Django 3.2.5 on 2022-02-04 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgnizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'City'},
        ),
        migrations.AlterModelOptions(
            name='courseorg',
            options={'verbose_name': 'Orgnization', 'verbose_name_plural': 'Orgnization'},
        ),
    ]