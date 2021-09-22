# Generated by Django 3.2.7 on 2021-09-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210908_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.Relations', to='articles.Scope', verbose_name='Темы статьи'),
        ),
    ]
