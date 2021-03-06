# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 01:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('cns', models.CharField(blank=True, max_length=15, null=True, verbose_name='CNS')),
                ('sexo', models.CharField(blank=True, max_length=10, null=True, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('pessoa', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao', models.CharField(max_length=50, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=20)),
                ('cbo', models.IntegerField(blank=True, null=True, verbose_name='CBO')),
                ('n_conselho', models.IntegerField(blank=True, null=True, verbose_name='Conselho de Classe')),
                ('admissao', models.DateField(default=django.utils.timezone.now)),
                ('ativo', models.BooleanField(default=False)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='complemento',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.Endereco'),
        ),
        migrations.AddField(
            model_name='complemento',
            name='pessoa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa'),
        ),
    ]
