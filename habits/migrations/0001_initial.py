# Generated by Django 4.2.7 on 2024-03-05 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='место')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата')),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('is_pleasurable', models.BooleanField(default=False, verbose_name='приятная привычка')),
                ('frequency', models.CharField(choices=[('day', 'раз в день'), ('week', 'раз в неделю')], default='day', max_length=50, verbose_name='периодичность')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='вознаграждение')),
                ('time_required', models.DurationField(default=60, verbose_name='время выполнения')),
                ('is_public', models.BooleanField(default=False, verbose_name='публичная привычка')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ('date',),
            },
        ),
    ]
