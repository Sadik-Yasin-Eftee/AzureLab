# Generated by Django 4.1.1 on 2022-10-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_instit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
    ]
