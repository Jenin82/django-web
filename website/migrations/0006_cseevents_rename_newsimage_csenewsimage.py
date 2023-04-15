# Generated by Django 4.1.7 on 2023-04-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_image_csedepartment_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='CseEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('poster', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('last_date', models.CharField(max_length=50)),
                ('google_form', models.CharField(max_length=300)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.RenameModel(
            old_name='NewsImage',
            new_name='CseNewsImage',
        ),
    ]
