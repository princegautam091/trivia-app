# Generated by Django 3.2.6 on 2021-12-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('quiz', '0003_rename_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op1', models.CharField(max_length=50)),
                ('op2', models.CharField(max_length=50)),
                ('op3', models.CharField(max_length=50)),
                ('op4', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op1', models.CharField(max_length=50)),
                ('op2', models.CharField(max_length=50)),
                ('op3', models.CharField(max_length=50)),
                ('op4', models.CharField(max_length=50)),
            ],
        ),
    ]
