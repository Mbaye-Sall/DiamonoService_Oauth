# Generated by Django 4.1.6 on 2023-02-09 02:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authServ', '0004_alter_address_code_alter_client_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='code',
            field=models.UUIDField(default=uuid.UUID('af1926be-71e1-4955-9256-6d8e2b90ce0b')),
        ),
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.UUIDField(default=uuid.UUID('87ddd596-4308-4448-9ec4-0b9b722715b3')),
        ),
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.UUIDField(default=uuid.UUID('c93e4382-98ce-426d-b563-05ab0d6dae38')),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.UUIDField(default=uuid.UUID('1897e300-cbc4-49d1-8e6e-97f8b85c560d')),
        ),
    ]
