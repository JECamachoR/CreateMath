# Generated by Django 3.1.5 on 2021-01-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210119_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='estatus_de_inscripcion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='primaria_o_secundaria',
            field=models.IntegerField(),
        ),
    ]
