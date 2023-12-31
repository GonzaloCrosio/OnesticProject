# Generated by Django 4.2.3 on 2023-08-10 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dateapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='update_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='dateapp.category', verbose_name='Categorías'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
