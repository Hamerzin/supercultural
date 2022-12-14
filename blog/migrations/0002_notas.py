# Generated by Django 4.1.2 on 2022-10-27 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('short_desciption', models.CharField(blank=True, max_length=400, null=True, unique=True)),
                ('image1', models.ImageField(upload_to='notas/')),
                ('image2', models.ImageField(upload_to='notas/')),
                ('image3', models.ImageField(upload_to='notas/')),
                ('image4', models.ImageField(upload_to='notas/')),
                ('image5', models.ImageField(upload_to='notas/')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('visit_num', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas_posts', to=settings.AUTH_USER_MODEL)),
                ('bio', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notas_bio', to='blog.profile')),
                ('categories', models.ManyToManyField(related_name='notas_posts', to='blog.category_post')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
