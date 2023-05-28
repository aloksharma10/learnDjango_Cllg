# Generated by Django 4.1.7 on 2023-05-28 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eno', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=10)),
                ('gender', models.CharField(default='', max_length=10)),
                ('img', models.ImageField(default='', upload_to='static/assets/img')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.role')),
            ],
        ),
    ]