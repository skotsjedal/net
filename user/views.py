from django.views import generic
from user.models import UserProfile
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class DetailView(generic.DetailView):
    template_name = 'user/detail.html'
    model = UserProfile

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.id == self.request.user.id and not self.request.user.is_staff:
            return HttpResponseRedirect(reverse('permission-error'))
        return super(DetailView, self).dispatch(request, *args, **kwargs)


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return UserProfile.objects.order_by('username')
