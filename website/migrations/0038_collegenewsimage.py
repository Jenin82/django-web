# Generated by Django 4.1.7 on 2023-04-21 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_remove_collegenews_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeNewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=300, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('collegeNews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collegeimages', to='website.collegenews')),
            ],
        ),
    ]
