# Generated by Django 5.1.1 on 2024-09-05 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
