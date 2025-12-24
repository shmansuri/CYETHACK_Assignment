from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import AlertModel
from .serializers import AlertSerializers
from .permissions import IsAdminOrReadOnly

class AlertViewSet(ModelViewSet):

    queryset = AlertModel.objects.select_related('event').order_by('-created_at')
    serializer_class = AlertSerializers
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'event__severity']

