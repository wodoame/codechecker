# Generated by Django 4.2.3 on 2023-10-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codechecker', '0002_record_no_of_uses'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='number',
            field=models.CharField(default='No number given', max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='no_of_uses',
            field=models.IntegerField(default=0),
        ),
    ]