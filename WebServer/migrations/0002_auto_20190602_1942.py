# Generated by Django 2.2.1 on 2019-06-02 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebServer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='headers',
            new_name='Headers',
        ),
    ]
