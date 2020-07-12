# Generated by Django 3.0.7 on 2020-07-12 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspaces', '0013_workspace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='people',
            field=models.ManyToManyField(related_name='organization_people', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspace_organization', to='workspaces.Organization'),
        ),
    ]
