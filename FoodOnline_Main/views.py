from django.http import HttpResponse
from django.http import request

def home(request):
    return HttpResponse('home')