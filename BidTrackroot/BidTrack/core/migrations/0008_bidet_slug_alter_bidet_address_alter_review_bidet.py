# Generated by Django 5.0.7 on 2024-07-16 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_bidet_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bidet',
            name='address',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='review',
            name='bidet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.bidet'),
        ),
    ]
