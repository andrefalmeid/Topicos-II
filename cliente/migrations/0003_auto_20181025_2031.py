# Generated by Django 2.1.2 on 2018-10-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='peso',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='Quantidade',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Quantidade'),
        ),
    ]
