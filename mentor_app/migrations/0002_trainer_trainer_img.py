# Generated by Django 4.0.4 on 2022-06-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='trainer_img',
            field=models.ImageField(default=0, upload_to='trainer'),
            preserve_default=False,
        ),
    ]
