# Generated by Django 5.0.6 on 2024-07-07 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='cupos',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
    ]
