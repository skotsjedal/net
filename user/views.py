from django.views import generic
from django.conf import settings
from user.models import UserProfile


class DetailView(generic.DetailView):
    template_name = 'user/detail.html'
    model = settings.AUTH_USER_MODEL


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return UserProfile.objects.order_by('username')
