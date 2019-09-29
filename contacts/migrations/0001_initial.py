# Generated by Django 2.2.5 on 2019-09-28 21:11

import contacts.contacts_register.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', contacts.contacts_register.models.ZipCodeField(max_length=9, null=True, verbose_name='CEP')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Endereço')),
                ('number', models.CharField(max_length=5, null=True, verbose_name='Número')),
                ('complement', models.CharField(max_length=25, null=True, verbose_name='Complemento')),
                ('district', models.CharField(max_length=50, null=True, verbose_name='Bairro')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='Município')),
                ('state', contacts.contacts_register.models.StateField(max_length=2, null=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Endereço de email')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Telefone de contato')),
                ('is_adopter', models.BooleanField(choices=[(False, 'Não'), (True, 'Sim')], default=False)),
                ('type', models.CharField(blank=True, choices=[('volunteer', 'Voluntário'), ('donor', 'Doador'), ('vet', 'Veterinário'), ('partner', 'Parceiro')], max_length=12, null=True, verbose_name='Tipo de contato')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.Person')),
            ],
            options={
                'permissions': (('access_contact', 'Acessar Contatos'),),
            },
        ),
    ]