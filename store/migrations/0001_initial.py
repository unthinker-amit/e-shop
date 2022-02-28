# Generated by Django 4.0.1 on 2022-02-24 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads/product/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]