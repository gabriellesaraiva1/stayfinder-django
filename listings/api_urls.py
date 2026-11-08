from rest_framework.routers import DefaultRouter
from .api import ListingViewSet
router = DefaultRouter()
router.register("hospedagens", ListingViewSet, basename="api-listing")
urlpatterns = router.urls
