from django.contrib import admin
from .models import ServiceRequest, SupportTicket

admin.site.register(ServiceRequest)
admin.site.register(SupportTicket)
