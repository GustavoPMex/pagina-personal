# Generated by Django 2.2.6 on 2019-10-22 02:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191021_2101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='description',
            options={'verbose_name': 'description', 'verbose_name_plural': 'descriptions'},
        ),
        migrations.AddField(
            model_name='description',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='description',
            name='upgrade',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AlterModelTable(
            name='description',
            table=None,
        ),
    ]
