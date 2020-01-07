# Generated by Django 2.2.4 on 2019-09-09 18:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('cd_comprador', models.AutoField(primary_key=True, serialize=False)),
                ('cd_cnpj', models.CharField(max_length=20)),
                ('cd_eancomprador', models.CharField(max_length=15)),
                ('nm_razaosocial', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('cd_fornecedor', models.AutoField(primary_key=True, serialize=False)),
                ('cd_cnpj', models.CharField(max_length=20)),
                ('cd_eanfornecedor', models.CharField(max_length=15)),
                ('nm_razaosocial', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('cd_produto', models.AutoField(primary_key=True, serialize=False)),
                ('ds_produto', models.CharField(max_length=200)),
                ('ds_ean_dun', models.CharField(max_length=15)),
                ('ds_und_medida', models.CharField(max_length=10)),
                ('qt_embalagem', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('cd_order', models.AutoField(primary_key=True, serialize=False)),
                ('cd_pedido', models.CharField(max_length=20)),
                ('vl_pedido', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ds_tipopedido', models.CharField(default='', max_length=10)),
                ('ds_funcao', models.CharField(default='', max_length=10)),
                ('qt_itens', models.IntegerField()),
                ('dt_emissao', models.DateField(blank=True, default=datetime.datetime.now)),
                ('ds_condicaoentrega', models.CharField(default='', max_length=10)),
                ('dt_entregainicio', models.DateField(blank=True, default=datetime.datetime.now)),
                ('dt_entregafinal', models.DateField(blank=True, default=datetime.datetime.now)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Comprador')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_itempedido', models.IntegerField()),
                ('qt_itenspedido', models.IntegerField()),
                ('vl_itempedido', models.DecimalField(decimal_places=2, max_digits=8)),
                ('vl_descontoitem', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Produto')),
            ],
        ),
    ]
