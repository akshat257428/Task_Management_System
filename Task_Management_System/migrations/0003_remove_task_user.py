# Generated by Django 5.1.5 on 2025-01-30 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Management_System', '0002_alter_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
