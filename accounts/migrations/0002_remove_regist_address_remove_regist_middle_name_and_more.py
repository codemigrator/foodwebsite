# Generated by Django 4.1.1 on 2022-09-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regist',
            name='address',
        ),
        migrations.RemoveField(
            model_name='regist',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='regist',
            name='password1',
        ),
        migrations.AddField(
            model_name='regist',
            name='password',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='regist',
            name='password2',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='regist',
            name='username',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
