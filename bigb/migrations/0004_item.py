# Generated by Django 2.1 on 2018-08-17 13:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigb', '0003_auto_20180815_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('qty', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigb.user')),
            ],
        ),
    ]
