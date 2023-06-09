# Generated by Django 4.1.7 on 2023-04-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0040_rename_mcadepartment_mbanewsimage_mbadepartment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_picture', models.CharField(max_length=300)),
                ('role', models.CharField(max_length=100)),
                ('placed_at', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
