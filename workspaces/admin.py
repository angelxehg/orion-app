from django.contrib import admin
from .models import Organization, Workspace, Group

admin.site.register(Organization)
admin.site.register(Workspace)
admin.site.register(Group)
