from rest_framework.routers import DefaultRouter
from main.views import UsuarioViewSet
from main.views import UsuarioRedeSocialViewSet

app_name = 'main'

router = DefaultRouter(trailing_slash=False)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'usuariosredesocial', UsuarioRedeSocialViewSet)

urlpatterns = router.urls

