# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoIdeb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Nome da Escola', max_length=500)),
                ('data', models.DateField(blank=True, verbose_name='Data', null=True)),
                ('resultado', models.DecimalField(blank=True, max_digits=8, decimal_places=5, verbose_name='Resultado Observado', null=True)),
                ('meta', models.DecimalField(blank=True, max_digits=8, decimal_places=5, verbose_name='Meta Projetado', null=True)),
            ],
            options={
                'verbose_name_plural': 'Resultado da Tabelas',
                'verbose_name': 'Resultado da Tabela',
                'ordering': ['nome'],
            },
        ),
    ]
