# Generated by Django 2.2.6 on 2020-01-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='visitors',
            field=models.ManyToManyField(to='main_app.Visitor'),
        ),
    ]
