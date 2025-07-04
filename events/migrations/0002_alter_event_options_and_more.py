# Generated by Django 5.2.3 on 2025-06-30 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created_at', 'start_datetime']},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_time',
            new_name='start_datetime',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.AddField(
            model_name='event',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
