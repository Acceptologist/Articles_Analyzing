# Generated by Django 2.1.3 on 2018-11-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=100)),
                ('Password.html', models.CharField(max_length=40)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
