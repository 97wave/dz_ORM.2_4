# Generated by Django 3.1.2 on 2021-09-12 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20210912_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
            ],
            options={
                'verbose_name': 'Тема статьи',
                'verbose_name_plural': 'Темы статьи',
                'ordering': ['-is_main'],
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
        migrations.DeleteModel(
            name='Relations',
        ),
        migrations.AddField(
            model_name='relationship',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Статья'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='scopes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope', verbose_name='Раздел'),
        ),
        migrations.AddField(
            model_name='article',
            name='relation',
            field=models.ManyToManyField(through='articles.Relationship', to='articles.Scope', verbose_name='Темы статьи'),
        ),
    ]
