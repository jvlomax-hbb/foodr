# Generated by Django 4.1.7 on 2023-03-08 21:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0009_alter_ingredient_ingredient_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="portions",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]