# Generated by Django 4.0.4 on 2022-04-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('bio', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
