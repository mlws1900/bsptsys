# Generated by Django 2.2.7 on 2020-01-29 18:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_celery_results', '0004_auto_20190516_0412'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('userTask_id', models.AutoField(primary_key=True, serialize=False, verbose_name='关联序号')),
                ('date_start', models.DateTimeField(default=datetime.datetime(2020, 1, 29, 18, 56, 29, 998605), verbose_name='任务开始时间')),
                ('userTask_task', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='django_celery_results.TaskResult', verbose_name='任务ID')),
                ('userTask_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户ID')),
            ],
        ),
    ]
