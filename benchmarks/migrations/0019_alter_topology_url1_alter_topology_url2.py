# Generated by Django 5.0.4 on 2024-07-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmarks', '0018_alter_topology_physical_qubits_per_cell_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topology',
            name='url1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='topology',
            name='url2',
            field=models.URLField(blank=True, null=True),
        ),
    ]
