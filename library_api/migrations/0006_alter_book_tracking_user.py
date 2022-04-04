# Generated by Django 4.0.3 on 2022-04-02 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0005_alter_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_tracking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_tracking', to=settings.AUTH_USER_MODEL),
        ),
    ]