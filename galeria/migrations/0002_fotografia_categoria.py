# Generated by Django 4.2.13 on 2024-05-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'nebulosa'), ('ESTRELA', 'estrela'), ('GALÁXIA', 'galáxia'), ('PLANETA', 'planeta')], default='', max_length=100),
        ),
    ]