# Generated by Django 3.0.3 on 2020-03-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0002_auto_20200327_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='repertoireID',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='sousserie',
            name='repertoireID',
            field=models.CharField(default='', max_length=20),
        ),
    ]
