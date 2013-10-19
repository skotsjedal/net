from django.conf.urls import patterns, include, url, handler404, handler500, handler403
from home import views as home
from blog import views as blog
from user import views as user
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', home.IndexView.as_view(), name='index'),

                       url(r'^blog/$', blog.IndexView.as_view(), name='blog'),
                       url(r'^blog/(?P<pk>\d+)/$', blog.DetailView.as_view(), name='blog'),
                       url(r'^blog/new$', blog.CreateView.as_view(), name='create-post'),
                       url(r'^blog/edit/(?P<pk>\d+)/$', blog.EditView.as_view(), name='edit-post'),
                       url(r'^blog/delete/(?P<pk>\d+)/$', blog.DeleteView.as_view(), name='delete-post'),
                       url(r'^blog/newcomment$', blog.CreateCommentView.as_view(), name='create-comment'),

                       url(r'^user/$', user.IndexView.as_view(), name='users'),
                       url(r'^user/(?P<pk>\d+)/$', user.DetailView.as_view(), name='userdetail'),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

                       url(r'^error/$', home.error, name='error'),
                       url(r'^error/404$', home.not_found_error, name='404-error'),
                       url(r'^error/perm$', home.perm_error, name='permission-error'),

                       url(r'^admin/', include(admin.site.urls)),
)

handler500 = 'home.views.error'
handler403 = 'home.views.error'
handler404 = 'home.views.not_found_error'