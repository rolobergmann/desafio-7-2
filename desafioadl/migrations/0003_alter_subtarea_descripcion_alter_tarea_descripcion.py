# Generated by Django 5.0.4 on 2024-04-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafioadl', '0002_alter_subtarea_id_alter_tarea_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtarea',
            name='descripcion',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(default='', max_length=255),
        ),
    ]
