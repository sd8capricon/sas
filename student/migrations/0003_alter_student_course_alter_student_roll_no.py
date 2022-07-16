# Generated by Django 4.0.5 on 2022-07-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('student', '0002_delete_assigncourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(blank=True, to='course.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]