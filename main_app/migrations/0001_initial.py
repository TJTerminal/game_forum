<<<<<<< HEAD
# Generated by Django 3.0.4 on 2020-05-04 18:04
=======
# Generated by Django 3.0.4 on 2020-05-04 18:05
>>>>>>> 2e45e2d67191eb4c7d32dcb41a5f36d4ca5ce0f3

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
    ]
