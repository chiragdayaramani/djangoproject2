# Generated by Django 3.2.6 on 2021-09-04 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='deleted_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
