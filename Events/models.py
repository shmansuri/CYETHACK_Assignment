from django.db import models

# Create your models here.

class Event(models.Model):
    severity_choice =(
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical')
    )

    sourceName = models.CharField(max_length=30 )
    eventType = models.CharField(max_length=30)
    severity = models.CharField(max_length=20, choices=severity_choice)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes =[
            models.Index(fields = ['severity']),
            models.Index(fields=['created_at'])
        ]

    def __str__(self):
        return f"{self.eventType} - {self.severity}"