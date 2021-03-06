# Generated by Django 3.1.4 on 2021-01-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='date',
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.DateField(),
        ),
    ]
