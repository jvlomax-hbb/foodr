# Generated by Django 4.1.7 on 2023-02-20 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredientgroup_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='ingredientGroup',
        ),
    ]