# Generated by Django 4.2.1 on 2023-10-26 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chef_info', '0006_feedback_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whislist',
            name='recipe_name',
        ),
        migrations.RemoveField(
            model_name='whislist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Feedback_new',
        ),
        migrations.DeleteModel(
            name='Whislist',
        ),
    ]
