# Generated by Django 3.0.2 on 2020-03-06 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0002_auto_20200306_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('W_id', models.AutoField(primary_key=True, serialize=False)),
                ('W_name', models.CharField(max_length=100)),
                ('W_skill', models.CharField(max_length=100)),
                ('W_link', models.CharField(max_length=300)),
                ('W_pic', models.CharField(max_length=100)),
                ('L_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CV.Legends')),
            ],
        ),
    ]
