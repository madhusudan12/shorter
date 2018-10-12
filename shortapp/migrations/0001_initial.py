# Generated by Django 2.1.1 on 2018-10-09 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=256)),
                ('profile_image', models.ImageField(upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='post_images')),
                ('time', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortapp.Member')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortapp.Member'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortapp.Post'),
        ),
        migrations.AddField(
            model_name='clap',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortapp.Member'),
        ),
        migrations.AddField(
            model_name='clap',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortapp.Post'),
        ),
    ]
