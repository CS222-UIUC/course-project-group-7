# Generated by Django 3.2.9 on 2022-11-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('major', models.CharField(max_length=150, null=True)),
                ('hobbies', models.CharField(max_length=300, null=True)),
                ('classes', models.CharField(max_length=150, null=True)),
                ('social_media', models.CharField(max_length=300, null=True)),
                ('email', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
