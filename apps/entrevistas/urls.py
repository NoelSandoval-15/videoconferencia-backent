from rest_framework.routers import DefaultRouter

from .views import EntrevistaViewSet, InvitadoViewSet

router = DefaultRouter()
router.register("entrevistas", EntrevistaViewSet, basename="entrevistas")
router.register("invitados", InvitadoViewSet, basename="invitados")

urlpatterns = router.urls
