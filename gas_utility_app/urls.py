from django.urls import path
from . import views

urlpatterns = [
    path('create_request/', views.create_service_request, name='create_request'),
    path('request_tracking/', views.request_tracking, name='request_tracking'),
    path('support_ticket/<int:request_id>/', views.support_ticket, name='support_ticket'),
]
