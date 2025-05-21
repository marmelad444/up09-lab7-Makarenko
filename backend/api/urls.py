from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)