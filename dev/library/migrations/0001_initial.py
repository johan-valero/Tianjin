# Generated by Django 3.2.12 on 2022-05-06 10:13

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=50)),
                ('firstname_author', models.CharField(max_length=50)),
                ('birthdate_author', models.DateField(verbose_name="Date de naissance du l'auteur")),
                ('picture_author', models.ImageField(blank=True, upload_to='pictures_author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Langage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_langage', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=50)),
                ('date_book', models.DateField(verbose_name='Date de publication')),
                ('synopsis_book', models.TextField(blank=True, null=True)),
                ('picture_book', models.ImageField(blank=True, upload_to='pictures_book')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
                ('category', models.ManyToManyField(to='library.Category')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.langage')),
            ],
        ),
    ]
