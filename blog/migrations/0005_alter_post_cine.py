# Generated by Django 4.1.2 on 2022-10-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_cines_descripcion_alter_teatros_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cine',
            field=models.ManyToManyField(blank=True, null=True, related_name='cines', to='blog.cines'),
        ),
    ]
