# Generated by Django 3.1.1 on 2020-09-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_lib', '0005_auto_20200917_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='pub_date',
            field=models.DateField(default='1991-1-1', verbose_name='publication date'),
        ),
    ]
