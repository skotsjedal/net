from django.views import generic
from blogg.models import *

class IndexView(generic.ListView):
    template_name = 'blogg/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-time')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogg/post.html'