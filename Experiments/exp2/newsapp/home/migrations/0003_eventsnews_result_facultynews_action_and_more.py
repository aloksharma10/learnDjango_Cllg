# Generated by Django 4.1.7 on 2023-04-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_eventsnews_img_facultynews_img_studentnews_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsnews',
            name='result',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='facultynews',
            name='action',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='studentnews',
            name='action',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='studentnews',
            name='result',
            field=models.TextField(default=''),
        ),
    ]
