# Generated by Django 4.1.2 on 2022-10-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_teatro_post_teatro'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hora',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]