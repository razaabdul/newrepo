# Generated by Django 4.0 on 2024-03-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=30)),
                ('star', models.IntegerField()),
            ],
        ),
    ]
