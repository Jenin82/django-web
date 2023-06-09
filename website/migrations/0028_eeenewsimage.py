# Generated by Django 4.1.7 on 2023-04-19 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_merge_0026_civilnewsimage_0026_eeenews'),
    ]

    operations = [
        migrations.CreateModel(
            name='EeeNewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=300, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('eeeDepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eeeimages', to='website.eeenews')),
            ],
        ),
    ]
