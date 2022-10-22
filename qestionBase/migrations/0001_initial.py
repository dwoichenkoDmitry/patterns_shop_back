# Generated by Django 4.0.4 on 2022-06-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('wayCalling', models.CharField(max_length=20, verbose_name='callType')),
                ('callRealize', models.CharField(max_length=255, verbose_name='call realize')),
                ('questionText', models.CharField(max_length=255, verbose_name='question text')),
            ],
        ),
    ]
