# Generated by Django 3.2.7 on 2021-09-17 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
                ('c_code', models.CharField(max_length=10)),
                ('seat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semeter', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=200)),
                ('last', models.CharField(max_length=200)),
                ('enroll', models.ManyToManyField(blank=True, related_name='enroll', to='regis.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='semeter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_semeter', to='regis.term'),
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_year', to='regis.term'),
        ),
    ]
