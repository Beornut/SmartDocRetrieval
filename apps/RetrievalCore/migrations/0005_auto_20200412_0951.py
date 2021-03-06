# Generated by Django 2.0 on 2020-04-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RetrievalCore', '0004_dvectorrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='default_precision',
            field=models.FloatField(blank=True, null=True, verbose_name='默认文档流顺序的准确率'),
        ),
        migrations.AlterField(
            model_name='session',
            name='precision',
            field=models.FloatField(blank=True, null=True, verbose_name='此session的准确率'),
        ),
    ]
