# Generated by Django 3.2.16 on 2023-01-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='picture', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
