# Generated by Django 4.1.2 on 2022-10-25 04:23

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_user_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profilepic",
            field=models.ImageField(upload_to=api.models.save_image),
        ),
    ]
