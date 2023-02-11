# Generated by Django 4.1.6 on 2023-02-05 23:49

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('code', models.UUIDField(default=uuid.UUID('32f88dd7-09fa-4390-bd93-0b3c4cdfe092'))),
                ('detail', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('phoneNo', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=255)),
                ('code', models.UUIDField(default=uuid.UUID('30096b47-d494-4540-a927-7225659e8707'))),
                ('dateOfBith', models.DateField(null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authServ.address')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pIdCard1', models.CharField(max_length=500)),
                ('code', models.UUIDField(default=uuid.UUID('855db08d-9344-4e7d-afb9-caca294a2078'))),
                ('pIdCard2', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authServ.user')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pIdCard1', models.CharField(max_length=500)),
                ('code', models.UUIDField(default=uuid.UUID('07971ef0-bd1f-4abe-9690-5e72394388bf'))),
                ('pIdCard2', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authServ.user')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField(default=0.0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authServ.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phoneNo', models.CharField(max_length=30)),
                ('identifiant', models.CharField(max_length=100, null=True)),
                ('blocked', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
                ('removed', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=10)),
                ('lastActivity', models.DateTimeField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('lastIpAddress', models.CharField(max_length=19)),
                ('lng', models.FloatField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
