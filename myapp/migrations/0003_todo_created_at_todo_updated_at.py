# Generated by Django 5.0.6 on 2025-01-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_alter_todo_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="todo",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
