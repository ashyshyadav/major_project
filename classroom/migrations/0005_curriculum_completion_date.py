# Generated by Django 4.0 on 2022-03-26 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_alter_curriculum_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='completion_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 26, 20, 18, 11, 8596), null=True),
        ),
    ]
