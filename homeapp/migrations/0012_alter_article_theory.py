# Generated by Django 3.2.4 on 2021-06-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0011_alter_article_theory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='theory',
            field=models.TextField(blank=True, null=True),
        ),
    ]
