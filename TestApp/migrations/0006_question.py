# Generated by Django 3.0.8 on 2021-04-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestApp', '0005_auto_20210319_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Questions', models.CharField(max_length=30)),
                ('Answers', models.CharField(max_length=30)),
            ],
        ),
    ]