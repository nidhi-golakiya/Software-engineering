# Generated by Django 3.0.4 on 2020-05-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0023_viewapplicants'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewapplicants',
            name='va_resume',
            field=models.FileField(null=True, upload_to='static/Resume'),
        ),
    ]
