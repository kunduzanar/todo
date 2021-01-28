# Generated by Django 3.1.4 on 2021-01-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210128_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtititle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=150)),
                ('year', models.DateField()),
                ('is_favorites', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
