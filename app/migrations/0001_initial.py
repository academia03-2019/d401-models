# Generated by Django 2.2 on 2019-04-30 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dt_nascimento', models.DateField()),
                ('vivo', models.BooleanField(default=True)),
                ('nacionalidade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(choices=[('av', 'Aventura'), ('rl', 'Religioso'), ('aa', 'Autoajuda'), ('fc', 'Ficção'), ('sf', 'Ficção Científica'), ('tr', 'Terror'), ('hq', 'Histórias em Quadrinhos'), ('mg', 'Mangá'), ('rm', 'Romance'), ('bg', 'Biografia')], max_length=2)),
                ('dt_lancamento', models.DateField()),
                ('descricao', models.TextField(default='')),
                ('editora', models.CharField(default='', max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('paginas', models.IntegerField()),
                ('edicoes', models.IntegerField()),
                ('nome', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='app.Autor')),
            ],
        ),
    ]
