# Generated by Django 4.2.5 on 2023-10-07 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('junior', 'Junior'), ('middle', 'Middle'), ('senior', 'Senior')], default='junior', max_length=255)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancyapp.company')),
                ('languages', models.ManyToManyField(related_name='vacancies', to='vacancyapp.language')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
