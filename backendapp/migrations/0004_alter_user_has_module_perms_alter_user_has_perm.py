# Generated by Django 4.0.4 on 2022-05-04 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0003_user_has_module_perms_user_has_perm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='has_module_perms',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='has_perm',
            field=models.BooleanField(default=False),
        ),
    ]