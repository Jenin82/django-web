# Generated by Django 4.1.7 on 2023-04-18 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_mechnewsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechnewsimage',
            name='mechDepartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechimages', to='website.mechnews'),
        ),
    ]
