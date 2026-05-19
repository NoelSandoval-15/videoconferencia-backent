from rest_framework.routers import DefaultRouter

from .views import EntrevistaViewSet

router = DefaultRouter()
router.register("entrevistas", EntrevistaViewSet, basename="entrevistas")

urlpatterns = router.urls
