# Generated by Django 3.2 on 2021-04-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to='posts/'),
        ),
    ]
