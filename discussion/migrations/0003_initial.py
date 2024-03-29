# Generated by Django 4.0.4 on 2022-04-29 05:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0008_alter_curriculum_completion_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discussion', '0002_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
