# Generated by Django 5.0.4 on 2024-07-24 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmarks', '0020_alter_processor_notes_alter_processor_url1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateset',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gateset',
            name='url1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gateset',
            name='url2',
            field=models.URLField(blank=True, null=True),
        ),
    ]