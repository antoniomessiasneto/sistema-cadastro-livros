# Generated by Django 5.2.4 on 2025-07-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('ano_publicacao', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('quantidade_estoque', models.IntegerField(default=0)),
            ],
        ),
    ]
