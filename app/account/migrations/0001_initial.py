# Generated by Django 3.2.21 on 2023-10-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon nomresi')),
                ('email', models.EmailField(max_length=120, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Name')),
                ('surname', models.CharField(blank=True, max_length=40, null=True, verbose_name='Surname')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='Profile Image')),
                ('about', models.TextField(null=True)),
                ('present_work_space', models.CharField(max_length=100, null=True)),
                ('birthday', models.DateField(null=True)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('meet', models.CharField(max_length=20, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('password_reset_code', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_disable', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'MyUser',
                'verbose_name_plural': 'MyUser',
                'ordering': ['-timestamp'],
            },
        ),
    ]