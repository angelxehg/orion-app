from rest_framework import routers
from workspaces import views as workspace_view_sets

router = routers.DefaultRouter()
router.register(r'organizations', workspace_view_sets.OrganizationViewset)
