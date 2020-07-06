# Generated by Django 3.0.7 on 2020-07-06 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('platform', models.CharField(max_length=50, null=True)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('user', models.CharField(max_length=200)),
                ('saved', models.BooleanField(default=False)),
            ],
        ),
    ]
