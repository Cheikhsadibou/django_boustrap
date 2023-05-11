# Generated by Django 4.1.6 on 2023-03-18 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='list_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=120, verbose_name='nom vehicule')),
                ('Resumer', models.TextField(blank=True)),
                ('Photo', models.ImageField(upload_to='', verbose_name='photo')),
            ],
        ),
        migrations.CreateModel(
            name='Detail_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contenu', models.TextField(blank=True)),
                ('Auteur', models.CharField(max_length=60)),
                ('Date_creer', models.DateField(verbose_name='Date creer')),
                ('Date_mise_en_vente', models.DateTimeField(verbose_name='Date mise en vente')),
                ('list_car', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.list_car')),
            ],
        ),
    ]