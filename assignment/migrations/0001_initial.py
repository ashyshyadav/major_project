# Generated by Django 4.0.3 on 2022-04-11 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0008_alter_curriculum_completion_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('points', models.PositiveIntegerField(default=10)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.subject')),
            ],
        ),
    ]