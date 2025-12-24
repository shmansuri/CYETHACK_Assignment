from django.db import models
from Events.models import Event

# Create your models here.
class AlertModel(models.Model):
    statusChoice = (
        ('OPEN', 'Open'),
        ('ACKNOWLEDGED', 'Acknowleged'),
        ('RESOLVED', 'Resolved')
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='alerts')
    status=models.CharField(max_length=20, choices=statusChoice, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes=[
            models.Index(fields=['status']),
            models.Index(fields=['created_at'])
            
        ]
    
    def __str__(self):
        return f"Alert For Event{self.event.id} - {self.status}"

