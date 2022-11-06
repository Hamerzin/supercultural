# Generated by Django 4.1.2 on 2022-11-06 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_descripcion_imagen3_post_descripcion_imagen5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='descripcion_imagen10',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='descripcion_imagen11',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='descripcion_imagen6',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='descripcion_imagen7',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='descripcion_imagen8',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='descripcion_imagen9',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image10',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image11',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
