# Generated by Django 3.1.6 on 2021-02-08 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='text_files')),
                ('ret_file', models.FileField(blank=True, null=True, upload_to='results')),
                ('finish_flag', models.IntegerField(default=0)),
                ('username', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
