# Generated by Django 4.1.7 on 2023-04-22 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_eventsnews_result_facultynews_action_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsnews',
            name='action',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='facultynews',
            name='result',
            field=models.TextField(default=''),
        ),
    ]
