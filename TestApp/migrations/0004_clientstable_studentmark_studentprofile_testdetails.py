# Generated by Django 3.0.8 on 2021-03-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0003_auto_20210319_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact_number', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='studentMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default=0, max_length=120)),
                ('ques_paper_id', models.CharField(max_length=50)),
                ('marks', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('test_title', models.CharField(max_length=50)),
                ('client', models.CharField(default=None, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(default=None, max_length=200)),
                ('roll_NO', models.CharField(default=None, max_length=200)),
                ('client', models.CharField(default=None, max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=200, unique=True)),
                ('client_id', models.CharField(default=0, max_length=200)),
                ('test_tittle', models.CharField(max_length=200)),
                ('test_duration', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
