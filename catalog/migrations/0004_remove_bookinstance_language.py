# Generated by Django 4.0 on 2024-04-01 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_book_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='language',
        ),
    ]