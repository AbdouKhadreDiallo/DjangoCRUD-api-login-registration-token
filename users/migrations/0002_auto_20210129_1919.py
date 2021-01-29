# Generated by Django 3.1 on 2021-01-29 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_admin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='is_cm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='is_student',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='is_teacher',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
