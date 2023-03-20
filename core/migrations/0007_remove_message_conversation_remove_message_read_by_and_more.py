# Generated by Django 4.1.5 on 2023-03-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_conversation_conversation_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='message',
            name='read_by',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='current_status',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='eduacational_qualifications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='open_to_work',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
