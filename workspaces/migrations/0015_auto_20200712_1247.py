# Generated by Django 3.0.7 on 2020-07-12 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspaces', '0014_auto_20200712_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_organizations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='people',
            field=models.ManyToManyField(related_name='organizations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_workspaces', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspaces', to='workspaces.Organization'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='people',
            field=models.ManyToManyField(related_name='workspaces', to=settings.AUTH_USER_MODEL),
        ),
    ]