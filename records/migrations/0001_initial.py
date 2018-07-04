# Generated by Django 2.0.5 on 2018-06-24 15:05

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mountains', '0002_mountain_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='mountain_images/')),
                ('votes', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
                ('mountain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mountains.Mountain')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1024)),
                ('record', models.TextField()),
                ('votes', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to=settings.AUTH_USER_MODEL)),
                ('mountain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='mountains.Mountain')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('time', models.DateTimeField()),
                ('ele', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrailRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1024)),
                ('votes', models.IntegerField(default=0)),
                ('accumulated_heights', models.IntegerField()),
                ('accumulated_depths', models.IntegerField()),
                ('simplified_track', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trail_records', to=settings.AUTH_USER_MODEL)),
                ('mountain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trail_records', to='mountains.Mountain')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('provider', models.CharField(default='youtube', max_length=1024)),
                ('link', models.CharField(max_length=2048)),
                ('votes', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to=settings.AUTH_USER_MODEL)),
                ('mountain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='mountains.Mountain')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WayPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('ele', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('trail_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='records.TrailRecord')),
            ],
        ),
        migrations.AddField(
            model_name='trackpoint',
            name='trail_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackpoints', to='records.TrailRecord'),
        ),
    ]