# Generated by Django 3.2.13 on 2022-08-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='place',
            name='name',
            field=models.CharField(default=4545, max_length=250),
            preserve_default=False,
        ),
    ]
