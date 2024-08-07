# Generated by Django 5.0.4 on 2024-07-24 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmarks', '0019_alter_topology_url1_alter_topology_url2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processor',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='url1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processor',
            name='url2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='topology',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
