# Generated by Django 4.1.5 on 2023-01-28 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_rename_user_attendance_attendee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendees', to='events.attendance'),
        ),
    ]