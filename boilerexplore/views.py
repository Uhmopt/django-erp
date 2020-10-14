from django.shortcuts import render

# Create your views here.

# @login_required
def viewTemplate(request):
    return render(request, 'boiler_explore.html')