from rest_framework import serializers
from .models import AlertModel

class AlertSerializers(serializers.ModelSerializer):
    event_id = serializers.IntegerField(source='event.id', read_only=True)
    eventType = serializers.CharField(source='event.eventType', read_only=True)
    severity = serializers.CharField(source='event.severity', read_only=True)

    class Meta:
        model = AlertModel
        fields = ['id', 'event_id', 'eventType', 'severity', 'status', 'created_at']
