# Generated by Django 2.1.2 on 2018-10-20 23:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
    ]