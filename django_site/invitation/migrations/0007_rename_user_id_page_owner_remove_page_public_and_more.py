# Generated by Django 4.2.5 on 2023-09-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0006_page_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='user_id',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='page',
            name='public',
        ),
        migrations.AlterField(
            model_name='page',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]