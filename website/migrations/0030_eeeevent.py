# Generated by Django 4.1.7 on 2023-04-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_merge_0028_civilevent_0028_eeenewsimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='EeeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('poster', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('last_date', models.CharField(max_length=50)),
                ('google_form', models.CharField(blank=True, max_length=300, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
