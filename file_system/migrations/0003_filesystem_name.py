# Generated by Django 4.1.2 on 2022-10-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_system', '0002_alter_filesystem_directory'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesystem',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]