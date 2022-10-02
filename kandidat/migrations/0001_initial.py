# Generated by Django 4.1.1 on 2022-09-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kandidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vorname', models.CharField(default='', max_length=50)),
                ('Nachname', models.CharField(default='', max_length=50)),
                ('geschlecht', models.CharField(default='', max_length=10)),
                ('email', models.CharField(default='', max_length=200)),
                ('Nummer', models.CharField(default='', max_length=50)),
                ('Beschreibung', models.CharField(default='', max_length=800)),
                ('ist_erwachsene', models.BooleanField(default=False)),
            ],
        ),
    ]
