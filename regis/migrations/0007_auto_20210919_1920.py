# Generated by Django 3.2.7 on 2021-09-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0006_course_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='for_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
