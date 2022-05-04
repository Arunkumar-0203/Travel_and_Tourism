# Generated by Django 4.0.3 on 2022-04-27 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='food',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='guides',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.guide'),
        ),
    ]
