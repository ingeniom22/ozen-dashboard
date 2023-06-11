from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required
@csrf_exempt
def index(request):
    # Page from the theme
    return render(request, "pages/dashboard.html")

