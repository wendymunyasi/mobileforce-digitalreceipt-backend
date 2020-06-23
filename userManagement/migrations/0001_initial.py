# Generated by Django 3.0.7 on 2020-06-22 05:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=50, null=True, unique=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('registration_id', models.CharField(max_length=10000, null=True)),
                ('deviceType', models.CharField(default=None, max_length=10000, null=True)),
                ('active', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
