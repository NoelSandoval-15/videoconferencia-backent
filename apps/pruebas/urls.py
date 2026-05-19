from rest_framework.routers import DefaultRouter

from .views import PruebaEntrevistaViewSet, PruebaViewSet

router = DefaultRouter()
router.register("pruebas", PruebaViewSet, basename="pruebas")
router.register(
    "pruebas-entrevista",
    PruebaEntrevistaViewSet,
    basename="pruebas-entrevista",
)

urlpatterns = router.urls
