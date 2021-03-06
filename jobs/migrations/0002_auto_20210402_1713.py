# Generated by Django 3.0 on 2021-04-02 17:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='employee',
            field=models.ManyToManyField(blank=True, default=None, related_name='job_employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(default=None),
        ),
    ]
