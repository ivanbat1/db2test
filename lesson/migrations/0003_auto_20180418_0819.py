# Generated by Django 2.0.4 on 2018-04-18 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_auto_20180416_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.Article'),
        ),
    ]
