# Generated by Django 3.1.1 on 2020-09-20 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('create_date_time', models.DateTimeField(auto_now_add=True)),
                ('update_date_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='A', max_length=5)),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144)),
                ('subtitle', models.CharField(blank=True, max_length=144)),
                ('content', models.TextField()),
                ('mainimage', models.ImageField(null=True, upload_to='img')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
