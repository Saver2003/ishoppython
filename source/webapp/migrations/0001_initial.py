# Generated by Django 2.2 on 2021-12-23 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='Описание')),
                ('category', models.TextField(default='other', max_length=100, verbose_name='Категория')),
                ('remainder', models.PositiveIntegerField(blank=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]