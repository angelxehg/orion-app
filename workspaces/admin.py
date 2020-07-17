from django.contrib import admin
from workspaces.models import Organization, Workspace, Channel


admin.site.register(Organization)
admin.site.register(Workspace)
admin.site.register(Channel)
