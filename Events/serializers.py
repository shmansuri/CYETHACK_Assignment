from rest_framework import serializers
from .models import Event
from Alert.models import AlertModel

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields=['id', 'sourceName', 'eventType', 'severity','description', 'created_at']
        read_only_fields =['id','created_at']

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        if event.severity in ['HIGH', 'CRITICAL']:
            AlertModel.objects.create(event=event)

        return event
    


