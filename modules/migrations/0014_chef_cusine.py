# Generated by Django 4.2.1 on 2023-10-25 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0013_remove_recipes_protein_alter_recipes_nut'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='cusine',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
