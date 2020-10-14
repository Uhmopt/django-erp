from django.shortcuts import render

# Create your views here.

# @login_required
def viewTemplate(request):
    return render(request, 'wheather_explore.html')