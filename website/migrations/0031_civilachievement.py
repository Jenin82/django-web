# Generated by Django 4.1.7 on 2023-04-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_civilteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='CivilAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(max_length=800)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
