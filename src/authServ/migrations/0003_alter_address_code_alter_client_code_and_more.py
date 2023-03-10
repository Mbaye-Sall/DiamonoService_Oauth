# Generated by Django 4.1.6 on 2023-02-09 01:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authServ', '0002_useraccount_opt_alter_address_code_alter_client_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='code',
            field=models.UUIDField(default=uuid.UUID('82b9b53a-c00f-4964-9120-d1cdda227484')),
        ),
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.UUIDField(default=uuid.UUID('7ee0a546-2f9d-4bbc-b58c-a677e172678b')),
        ),
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.UUIDField(default=uuid.UUID('8e573103-f179-4961-a0fa-b63f5c7c4b34')),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.UUIDField(default=uuid.UUID('a4055546-3574-43e5-86b8-2937cc03155d')),
        ),
    ]
