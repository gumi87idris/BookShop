# Generated by Django 3.1 on 2022-01-19 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('last_name', models.CharField(blank=True, max_length=85)),
                ('date_of_Birth', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='authors')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('slug', models.SlugField(max_length=55, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='books')),
                ('status', models.CharField(choices=[('in stock', 'В наличии'), ('out of stock', 'Нет в наличии')], max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='main.author')),
                ('genre', models.ManyToManyField(to='main.Genre')),
            ],
        ),
    ]
