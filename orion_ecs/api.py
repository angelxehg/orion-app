from rest_framework import routers
from workspaces import viewsets as workspace_view_sets

router = routers.DefaultRouter()
router.register(r'organizations', workspace_view_sets.OrganizationViewset)
