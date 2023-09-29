# Generated by Django 4.2.5 on 2023-09-28 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invitation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='shared_users',
            field=models.ManyToManyField(related_name='shared_pages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='page',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]
