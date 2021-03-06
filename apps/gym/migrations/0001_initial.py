# Generated by Django 3.2.7 on 2022-02-17 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gyms', to=settings.AUTH_USER_MODEL, verbose_name='Boss of the Gym')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=64)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='gym.gym', verbose_name='Available subscriptions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='gym.gym', verbose_name='Gym')),
                ('subscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscribers', to='gym.subscription', verbose_name='Subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'unique_together': {('user', 'gym')},
            },
        ),
    ]
