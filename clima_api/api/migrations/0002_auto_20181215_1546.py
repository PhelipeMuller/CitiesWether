# Generated by Django 2.1.4 on 2018-12-15 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CityWether',
            new_name='CityWeather',
        ),
        migrations.AlterModelOptions(
            name='cityweather',
            options={'ordering': ['-created'], 'verbose_name': 'City Weather', 'verbose_name_plural': 'Cities Weather'},
        ),
    ]