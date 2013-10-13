from django.views import generic
from blogg.models import *
from django.core.urlresolvers import reverse
from blogg.form import NewBlog


class IndexView(generic.ListView):
    template_name = 'blogg/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.order_by('-time')[:5]
        return posts


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogg/post.html'


class CreateView(generic.CreateView):
    model = Post
    form_class = NewBlog
    template_name = 'blogg/create.html'

    def form_valid(self, form):
        print "form_valid"
        form.instance.author = self.request.user
        form.instance.time = datetime.now()
        return super(CreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blogg')

    #def get_context_data(self, **kwargs):
    #
    #    context = super(CreateView, self).get_context_data(**kwargs)
    #    context['action'] = reverse('createblogg')
    #    return context
