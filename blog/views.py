from django.views import generic
from blog.models import *
from django.core.urlresolvers import reverse, reverse_lazy
from blog.form import NewBlog, NewComment, UpdateBlog
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.order_by('-time')[:5]
        return posts


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/view.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.public and not self.request.user.is_staff:
            return HttpResponseRedirect(reverse('permission-error'))
        return super(DetailView, self).dispatch(request, *args, **kwargs)


class CreateView(generic.CreateView):
    model = Post
    form_class = NewBlog
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect(reverse('permission-error'))
        return super(CreateView, self).dispatch(request, *args, **kwargs)


class EditView(generic.UpdateView):
    model = Post
    form_class = UpdateBlog
    template_name = 'blog/create.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect(reverse('permission-error'))
        return super(EditView, self).dispatch(request, *args, **kwargs)


class DeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect(reverse('permission-error'))
        return super(DeleteView, self).dispatch(request, *args, **kwargs)


class CreateCommentView(generic.CreateView):
    model = Comment
    form_class = NewComment

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateCommentView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('permission-error'))
        return super(CreateCommentView, self).dispatch(request, *args, **kwargs)