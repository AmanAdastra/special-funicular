# Generated by Django 3.2.4 on 2021-06-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_alter_bucket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucket',
            name='user',
            field=models.IntegerField(default=1),
        ),
    ]
