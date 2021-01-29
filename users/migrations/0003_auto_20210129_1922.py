# Generated by Django 3.1 on 2021-01-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210129_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='is_admin',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_cm',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_student',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_teacher',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
