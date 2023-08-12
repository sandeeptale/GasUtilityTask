from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, SupportTicket
from .forms import ServiceRequestForm

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'create_request.html', {'form': form})

@login_required
def request_tracking(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'request_tracking.html', {'service_requests': service_requests})

@login_required
def support_ticket(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    if request.method == 'POST':
        message = request.POST['message']
        SupportTicket.objects.create(request=service_request, agent=request.user, message=message)
    return render(request, 'support_ticket.html', {'service_request': service_request})
