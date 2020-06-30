from rest_framework_nested import routers
from workspaces.views import OrganizationViewset, WorkspaceViewset, GroupViewset

router = routers.SimpleRouter()
router.register(r'organizations', OrganizationViewset)

organization_router = routers.NestedSimpleRouter(router, r'organizations', lookup='organization')
organization_router.register(r'workspaces', WorkspaceViewset)
organization_router.register(r'groups', GroupViewset)
