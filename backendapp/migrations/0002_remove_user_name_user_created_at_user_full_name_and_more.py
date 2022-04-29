# Generated by Django 4.0.4 on 2022-04-29 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_mover',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_date', models.DateField(auto_now_add=True, verbose_name='Conversation Date')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Conversation Date')),
                ('mover', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='move', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Move', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Email_msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_key', models.IntegerField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('from1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivingFrom', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sendingTo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
