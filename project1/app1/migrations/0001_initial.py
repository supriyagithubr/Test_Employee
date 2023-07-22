# Generated by Django 4.2.3 on 2023-07-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.IntegerField()),
                ('e_name', models.CharField(max_length=90)),
                ('salary', models.FloatField()),
                ('city', models.CharField(max_length=80)),
                ('c_name', models.CharField(max_length=70)),
            ],
        ),
    ]