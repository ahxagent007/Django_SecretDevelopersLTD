# Generated by Django 3.0.2 on 2020-01-14 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_detais',
            new_name='project_details',
        ),
    ]
