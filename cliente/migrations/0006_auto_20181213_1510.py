# Generated by Django 2.1.2 on 2018-12-13 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20181213_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='Quantidade',
            new_name='quantidade',
        ),
    ]
