# Generated by Django 4.1.2 on 2022-11-03 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_post_mp3_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favoritos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fav', to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fav', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
