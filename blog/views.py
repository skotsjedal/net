from django.views import generic
from blog.models import *
from django.core.urlresolvers import reverse, reverse_lazy
from blog.form import NewBlog, NewComment, UpdateBlog


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.order_by('-time')[:5]
        return posts


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/view.html'


class CreateView(generic.CreateView):
    model = Post
    form_class = NewBlog
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class EditView(generic.UpdateView):
    model = Post
    form_class = UpdateBlog
    template_name = 'blog/create.html'


class DeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog')


class CreateCommentView(generic.CreateView):
    model = Comment
    form_class = NewComment

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog')