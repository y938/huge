# Generated by Django 2.2 on 2020-11-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Earth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile'),
        ),
    ]
