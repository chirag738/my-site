# Generated by Django 5.0.2 on 2024-04-29 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_crimedetail_user_remove_yourdetail_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yourdetail',
            name='user_id',
        ),
    ]
