# Generated by Django 3.1.1 on 2020-09-03 03:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nim', models.CharField(default='', max_length=70)),
                ('name', models.TextField(default='')),
                ('departement', models.CharField(default='', max_length=70)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]
