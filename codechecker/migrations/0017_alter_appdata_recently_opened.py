# Generated by Django 4.2.3 on 2024-01-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codechecker', '0016_alter_appdata_recently_opened'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdata',
            name='recently_opened',
            field=models.JSONField(default=list),
        ),
    ]