# Generated by Django 3.2.7 on 2021-09-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0003_auto_20210917_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Number_of_Applicants',
            field=models.IntegerField(default=0),
        ),
    ]
