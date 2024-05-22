# Generated by Django 4.2.12 on 2024-05-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_room_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(max_length=200)),
                ('question', models.TextField(max_length=255)),
            ],
        ),
    ]
