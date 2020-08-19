from rest_framework_nested import routers
from workspaces.views import SearchViewset, OrganizationViewset, WorkspaceViewset, ChannelViewset, MessageViewset

router = routers.SimpleRouter()
router.register(r'search', SearchViewset)
router.register(r'organizations', OrganizationViewset)

organization_router = routers.NestedSimpleRouter(
    router, r'organizations', lookup='organization')
organization_router.register(r'workspaces', WorkspaceViewset)
organization_router.register(r'channels', ChannelViewset)

channel_router = routers.NestedSimpleRouter(
    organization_router, r'channels', lookup='channel')
channel_router.register(r'messages', MessageViewset)
