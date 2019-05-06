# Generated by Django 2.1.7 on 2019-05-01 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('record', '0005_auto_20190501_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='approve_status',
            field=models.IntegerField(choices=[(0, 'Rejected'), (1, 'Approve'), (2, 'Waiting')], default=2),
        ),
        migrations.AddField(
            model_name='record',
            name='create_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
