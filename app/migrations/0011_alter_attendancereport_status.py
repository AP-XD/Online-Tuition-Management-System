# Generated by Django 4.0 on 2022-04-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancereport',
            name='status',
            field=models.CharField(choices=[('1', 'present'), ('2', 'absent')], max_length=20),
        ),
    ]
