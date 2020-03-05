# Generated by Django 3.0.2 on 2020-01-14 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=250)),
                ('skill_logo', models.CharField(max_length=250)),
                ('skill_tag_line', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=250)),
                ('project_detais', models.CharField(max_length=500)),
                ('project_link', models.CharField(max_length=500)),
                ('project_pic', models.CharField(max_length=250)),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.Skills')),
            ],
        ),
    ]
