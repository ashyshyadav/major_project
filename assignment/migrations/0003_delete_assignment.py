# Generated by Django 4.0.4 on 2022-04-27 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_rename_name_assignment_title_assignment_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assignment',
        ),
    ]