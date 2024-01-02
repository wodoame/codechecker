# Generated by Django 4.2.3 on 2023-10-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('msisdn', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('attended', models.CharField(default='no', max_length=3)),
            ],
        ),
    ]