# Generated by Django 5.1.4 on 2025-01-08 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pehchan', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='job_company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='job_link',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='post',
            name='skill',
            field=models.TextField(max_length=2000),
        ),
    ]
