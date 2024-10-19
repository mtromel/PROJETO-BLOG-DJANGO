# Generated by Django 4.2.16 on 2024-10-19 12:54

from django.db import migrations, models
import django_summernote.utils


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_page_options_alter_page_is_published_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Defaults to filename, if left blank', max_length=255, null=True)),
                ('file', models.FileField(upload_to=django_summernote.utils.uploaded_filepath)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
