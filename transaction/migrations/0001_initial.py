# Generated by Django 3.2.10 on 2022-01-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('trans_id', models.BigIntegerField(default=1000000, primary_key=True, serialize=False)),
                ('amount', models.PositiveBigIntegerField(default=0)),
                ('sender', models.PositiveBigIntegerField(null=True)),
                ('receiver', models.PositiveBigIntegerField(null=True)),
            ],
        ),
    ]
