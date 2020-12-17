# Generated by Django 3.1.3 on 2020-11-25 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('date', models.CharField(db_index=True, max_length=100, verbose_name='Date')),
                ('time', models.CharField(db_index=True, max_length=100, verbose_name='Time')),
                ('duration', models.IntegerField(db_index=True, verbose_name='Duration')),
                ('doctor_name', models.CharField(db_index=True, max_length=100, verbose_name='Doctor_name')),
                ('department', models.CharField(db_index=True, max_length=100, verbose_name='Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]