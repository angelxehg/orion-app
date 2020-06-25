from rest_framework import routers
from rental import api_views as my_views
from workspaces import viewsets as workspace_viewsets

router = routers.DefaultRouter()
router.register(r'friends', my_views.FriendViewset)
router.register(r'belongings', my_views.BelongingViewset)
router.register(r'borrowings', my_views.BorrowedViewset)
router.register(r'organizations', workspace_viewsets.OrganizationViewset)
