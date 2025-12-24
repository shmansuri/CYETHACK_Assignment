from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializers
from .permissions import IsAdminOnly

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated, IsAdminOnly]
