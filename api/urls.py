from django.urls import include, path
from rest_framework import routers
from app.views import CategoriaViewSet, ClienteViewSet

router = routers.DefaultRouter()

router.register(r'categorias', CategoriaViewSet)
router.register(r'clientes', ClienteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]