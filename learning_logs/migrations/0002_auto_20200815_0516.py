# Generated by Django 3.1 on 2020-08-15 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='test',
            new_name='text',
        ),
    ]
