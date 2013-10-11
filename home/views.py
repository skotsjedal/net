__author__ = 'skotsj'
from django.http import HttpResponse


def index(request):
    return HttpResponse("frontpage")
