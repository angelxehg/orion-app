from rest_framework_nested import routers
from workspaces.views import OrganizationViewset

router = routers.SimpleRouter()
router.register(r'organizations', OrganizationViewset)
