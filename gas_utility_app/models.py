from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    TYPES = (
        ('Gas Leak', 'Gas Leak'),
        ('Meter Installation', 'Meter Installation'),
        
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPES, max_length=50)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')

class SupportTicket(models.Model):
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)






