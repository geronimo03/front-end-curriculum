# Generated by Django 3.0.8 on 2020-07-12 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='code',
        ),
        migrations.RemoveField(
            model_name='post',
            name='style',
        ),
    ]
