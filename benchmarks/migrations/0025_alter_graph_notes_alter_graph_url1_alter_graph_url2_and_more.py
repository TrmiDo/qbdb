# Generated by Django 4.2.14 on 2024-07-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmarks', '0024_rename_min_11_calibration_min_t1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='url1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='url2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='probleminstance',
            name='url1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='probleminstance',
            name='url2',
            field=models.URLField(blank=True, null=True),
        ),
    ]
