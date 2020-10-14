from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required
def viewTemplate(request, zone_id):
    return render(request, 'zone_monitor.html', dict(zone_id=zone_id))