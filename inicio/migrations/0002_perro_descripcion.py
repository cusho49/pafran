# Generated by Django 4.2.2 on 2023-06-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sugerencia',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
