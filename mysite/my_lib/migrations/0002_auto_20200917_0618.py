# Generated by Django 3.1.1 on 2020-09-17 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_lib', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='experience',
        ),
        migrations.AddField(
            model_name='document',
            name='document_genre',
            field=models.CharField(choices=[('SC', 'Scientific'), ('SF', 'Science fiction'), ('RM', 'Romance'), ('TR', 'Thriller'), ('DR', 'Drama'), ('TG', 'Tragic')], default='SC', max_length=2),
        ),
    ]
