# Generated by Django 4.1.5 on 2023-02-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_email', models.CharField(max_length=100)),
                ('check_in', models.CharField(max_length=50)),
                ('check_out', models.CharField(max_length=50)),
            ],
        ),
    ]
