# Generated by Django 4.2.6 on 2024-01-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0010_utilisateur_is_active_utilisateur_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='user_permissions',
        ),
    ]
