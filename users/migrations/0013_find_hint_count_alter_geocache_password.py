# Generated by Django 4.2.4 on 2023-11-25 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_geocache_hint_geocache_password_hint'),
    ]

    operations = [
        migrations.AddField(
            model_name='find',
            name='hint_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='geocache',
            name='password',
            field=models.CharField(max_length=12),
        ),
    ]
