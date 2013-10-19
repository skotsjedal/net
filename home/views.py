from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from skotsj.settings import STATIC_URL


class IndexView(TemplateView):
    template_name = 'home/index.html'


def error(request):
    return render_to_response('home/error/default.html', {'STATIC_URL': STATIC_URL})


def not_found_error(request):
    return render_to_response('home/error/404.html',  {'STATIC_URL': STATIC_URL})


def perm_error(request):
    return render_to_response('home/error/perm_error.html',  {'STATIC_URL': STATIC_URL})
