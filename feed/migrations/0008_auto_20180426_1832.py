# Generated by Django 2.0.1 on 2018-04-27 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_tag_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='can_help',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='tag',
            name='needs_help',
            field=models.BooleanField(default=0),
        ),
    ]
