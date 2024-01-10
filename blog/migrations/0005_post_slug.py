# Generated by Django 3.2.23 on 2024-01-09 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
