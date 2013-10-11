__author__ = 'skotsj'
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'
    #context_object_name = 'Index'

    def get(self, request, *args, **kwargs):
        context = 1
        return self.render_to_response(context)

