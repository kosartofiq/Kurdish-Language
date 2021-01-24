# Generated by Django 3.1.4 on 2021-01-18 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Langauge Name')),
                ('native_name', models.CharField(help_text="Name of language and written in native of it's Language", max_length=100, unique=True, verbose_name='Native Language Name')),
                ('iso_639_1', models.CharField(help_text='for more info: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes', max_length=2, unique=True, verbose_name='ISO 639-1')),
                ('iso_639_2', models.CharField(help_text='for more info: https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes', max_length=3, unique=True, verbose_name='ISO 639-2')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Edited Date')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='language_histories', related_query_name='language_history', to=settings.AUTH_USER_MODEL, verbose_name='Editor Id')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language_histories', related_query_name='language_history', to='language.language', verbose_name='Lanuage Id')),
            ],
            options={
                'verbose_name': 'language history',
                'verbose_name_plural': 'languages histories',
            },
        ),
    ]
