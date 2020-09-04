# Generated by Django 3.1.1 on 2020-09-04 07:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('filename', models.TextField(default='')),
                ('url', models.TextField(default='')),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.student', verbose_name='Student')),
            ],
        ),
    ]
