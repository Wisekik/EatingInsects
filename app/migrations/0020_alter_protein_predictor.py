# Generated by Django 4.1.5 on 2023-01-18 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_protein_predictor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein',
            name='predictor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.predictor'),
            preserve_default=False,
        ),
    ]
