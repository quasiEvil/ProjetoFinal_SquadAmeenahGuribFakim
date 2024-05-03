# Generated by Django 4.2.11 on 2024-04-12 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('raca', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=10)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('idade', models.IntegerField()),
                ('castrado', models.BooleanField(default=False)),
                ('data_entrada', models.DateTimeField(db_column='Data de Entrada', null=True, verbose_name='Data de Entrada')),
                ('historico_saude', models.TextField()),
                ('pelagem', models.CharField(choices=[('curto', 'Curto'), ('medio', 'Medio'), ('longo', 'Longo')], max_length=10)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='pets')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animais',
            },
        ),
    ]