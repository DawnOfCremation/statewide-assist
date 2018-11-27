# Generated by Django 2.0.2 on 2018-11-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='collapse_number',
            field=models.CharField(default='eg - collapseOne', max_length=50),
        ),
        migrations.AddField(
            model_name='faq',
            name='heading_number',
            field=models.CharField(default='eg - headingOne', max_length=50),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(default='add answer here', max_length=200),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(default='add question here', max_length=100),
        ),
    ]
