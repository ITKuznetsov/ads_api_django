from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Ad
from .serializers import AdSerializer
from .permissions import ReadOnly


class AdModelViewSet(ModelViewSet):
    queryset = Ad.objects.all().order_by('position')[:10]
    serializer_class = AdSerializer
    permission_classes = [ReadOnly]
    http_method_names = ['get']


class AdDetailViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [ReadOnly]
    http_method_names = ['get']


def IndexView(request):
    return render(request, 'ads/index.html')
