# Generated by Django 2.2.5 on 2019-09-30 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='username',
        ),
    ]
