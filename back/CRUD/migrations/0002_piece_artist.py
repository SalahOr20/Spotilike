# Generated by Django 4.2.6 on 2024-01-01 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CRUD.artist'),
            preserve_default=False,
        ),
    ]
