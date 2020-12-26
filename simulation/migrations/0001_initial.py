# Generated by Django 3.1.4 on 2020-12-20 20:56

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('simID', models.PositiveIntegerField()),
                ('hints', models.TextField(blank=True, null=True)),
                ('questions', models.TextField(blank=True, null=True)),
                ('tests', models.TextField(blank=True, null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=150, null=True)),
                ('score', models.IntegerField(default=50)),
                ('isFinished', models.BooleanField(default=False)),
                ('isDiagnosed', models.BooleanField(default=False)),
                ('isStarred', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=47)),
                ('desc', models.TextField()),
                ('difficulty', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('race', models.CharField(max_length=150)),
                ('birth', models.CharField(max_length=150)),
                ('weight', models.CharField(max_length=150)),
                ('height', models.CharField(max_length=150)),
                ('sexuallyActive', models.CharField(max_length=150)),
                ('medications', models.TextField(blank=True, null=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('illnesses', models.TextField(blank=True, null=True)),
                ('symptoms', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=150, null=True)),
                ('diagnosis', models.CharField(max_length=150)),
                ('test1', models.CharField(blank=True, max_length=150, null=True)),
                ('desc1', models.TextField(blank=True, null=True)),
                ('test1Res', models.CharField(blank=True, max_length=150, null=True)),
                ('test2', models.CharField(blank=True, max_length=150, null=True)),
                ('desc2', models.TextField(blank=True, null=True)),
                ('test2Res', models.CharField(blank=True, max_length=150, null=True)),
                ('test3', models.CharField(blank=True, max_length=150, null=True)),
                ('desc3', models.TextField(blank=True, null=True)),
                ('test3Res', models.CharField(blank=True, max_length=150, null=True)),
                ('test4', models.CharField(blank=True, max_length=150, null=True)),
                ('desc4', models.TextField(blank=True, null=True)),
                ('test4Res', models.CharField(blank=True, max_length=150, null=True)),
                ('test5', models.CharField(blank=True, max_length=150, null=True)),
                ('desc5', models.TextField(blank=True, null=True)),
                ('test5Res', models.CharField(blank=True, max_length=150, null=True)),
                ('test6', models.CharField(blank=True, max_length=150, null=True)),
                ('desc6', models.TextField(blank=True, null=True)),
                ('test6Res', models.CharField(blank=True, max_length=150, null=True)),
                ('tNum', models.IntegerField()),
                ('quest1', models.TextField(blank=True, null=True)),
                ('resp1', models.TextField(blank=True, null=True)),
                ('quest2', models.TextField(blank=True, null=True)),
                ('resp2', models.TextField(blank=True, null=True)),
                ('quest3', models.TextField(blank=True, null=True)),
                ('resp3', models.TextField(blank=True, null=True)),
                ('quest4', models.TextField(blank=True, null=True)),
                ('resp4', models.TextField(blank=True, null=True)),
                ('quest5', models.TextField(blank=True, null=True)),
                ('resp5', models.TextField(blank=True, null=True)),
                ('quest6', models.TextField(blank=True, null=True)),
                ('resp6', models.TextField(blank=True, null=True)),
                ('qNum', models.IntegerField()),
                ('hint1', models.TextField(blank=True, null=True)),
                ('hint2', models.TextField(blank=True, null=True)),
                ('hint3', models.TextField(blank=True, null=True)),
                ('hint4', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
