# Generated by Django 2.0.4 on 2018-04-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
                ('article_date', models.DateTimeField()),
                ('article_likes', models.IntegerField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
