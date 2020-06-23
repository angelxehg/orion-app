from rest_framework import routers
from core import views as my_views

router = routers.DefaultRouter()
router.register(r'friends', my_views.FriendViewset)
router.register(r'belongings', my_views.BelongingViewset)
router.register(r'borrowings', my_views.BorrowedViewset)
