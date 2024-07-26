from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdModelViewSet, AdDetailViewSet, IndexView

app_name = 'ads'

router = DefaultRouter()
router.register(r'ads', AdModelViewSet, basename='ad')
router.register(r'ad', AdDetailViewSet, basename='ad-detail')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', IndexView, name='index'),
]
