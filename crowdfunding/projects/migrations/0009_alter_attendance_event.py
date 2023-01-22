# Generated by Django 4.1.5 on 2023-01-22 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_event_owner_attendance_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='projects.event'),
        ),
    ]
