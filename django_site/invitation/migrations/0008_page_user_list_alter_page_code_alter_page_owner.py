# Generated by Django 4.2.5 on 2023-09-29 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invitation', '0007_rename_user_id_page_owner_remove_page_public_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='user_list',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessed_pages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='page',
            name='code',
            field=models.CharField(max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_pages', to=settings.AUTH_USER_MODEL),
        ),
    ]
