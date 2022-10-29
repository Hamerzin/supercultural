# Generated by Django 4.1.2 on 2022-10-28 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_linkyoutube'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='galeria/')),
                ('info', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
