# Generated by Django 4.1.7 on 2023-04-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_cseteacher_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cseteacher',
            name='role',
            field=models.CharField(choices=[('F', 'Faculty'), ('T', 'Technical Staff')], default='F', max_length=1),
        ),
    ]