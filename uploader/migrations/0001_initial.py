# Generated by Django 3.1.2 on 2020-10-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=150)),
                ('file_ne_name', models.CharField(max_length=200)),
                ('file_size', models.DecimalField(decimal_places=0, max_digits=10)),
                ('file_path', models.CharField(max_length=500)),
                ('upload_time', models.DateTimeField()),
                ('authorID', models.IntegerField()),
            ],
        ),
    ]
