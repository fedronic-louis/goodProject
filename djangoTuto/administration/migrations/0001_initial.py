# Generated by Django 4.0 on 2021-12-16 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='none', max_length=20)),
                ('nom', models.CharField(blank=True, default='none', max_length=500)),
                ('adresse', models.CharField(blank=True, default='none', max_length=500)),
                ('cp', models.CharField(blank=True, default='none', max_length=6)),
                ('commune', models.CharField(blank=True, default='none', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Grn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='none', max_length=20)),
                ('description', models.CharField(blank=True, default='none', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='none', max_length=20)),
                ('profile', models.IntegerField(blank=True, choices=[(0, 'Candidat'), (1, 'Formateur'), (2, 'Responsable de Formation'), (3, 'Assistante Technique'), (4, 'Autre4'), (5, 'Autre5'), (6, 'Autre6')], default=0, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
