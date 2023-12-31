# Generated by Django 4.2.5 on 2023-10-02 12:33

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invitation', '0008_page_user_list_alter_page_code_alter_page_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagePermission',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.permission')),
            ],
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='admin_list',
            field=models.ManyToManyField(related_name='admin_pages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='page',
            name='user_list',
        ),
        migrations.AddField(
            model_name='page',
            name='user_list',
            field=models.ManyToManyField(related_name='accessed_pages', to=settings.AUTH_USER_MODEL),
        ),
    ]
