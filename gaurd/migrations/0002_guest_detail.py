# Generated by Django 3.1.1 on 2020-10-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaurd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='guest_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intime', models.CharField(max_length=100)),
                ('extime', models.CharField(max_length=100)),
                ('guest', models.CharField(max_length=100)),
                ('pur', models.CharField(max_length=100)),
                ('camefrom', models.CharField(max_length=100)),
            ],
        ),
    ]
