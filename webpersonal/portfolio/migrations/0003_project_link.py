# Generated by Django 4.1.6 on 2023-02-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_alter_project_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]