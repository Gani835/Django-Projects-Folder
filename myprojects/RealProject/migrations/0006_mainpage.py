# Generated by Django 4.1 on 2022-09-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealProject', '0005_diary_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Textarea', models.TextField(max_length=10000)),
            ],
        ),
    ]
