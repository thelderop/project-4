# Generated by Django 3.1 on 2020-08-17 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('voting_record', models.TextField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='congress.state')),
            ],
        ),
        migrations.CreateModel(
            name='Senate_Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField(default='Healthcare is not as expensive as the corporate media might have you believe.')),
                ('senator', models.ManyToManyField(to='congress.Senator')),
            ],
        ),
    ]
