from django.views import generic

from user.models import UserProfile


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return UserProfile.objects.order_by('username')


class DetailView(generic.DetailView):
    model = UserProfile
    template_name = 'user/detail.html'