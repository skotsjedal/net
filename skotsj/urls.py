from django.conf.urls import patterns, include, url
from home import views as home
from blog import views as blog
from user import views as user
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', home.IndexView.as_view(), name='index'),
                       url(r'^blog/$', blog.IndexView.as_view(), name='blog'),
                       url(r'^blog/new$', blog.CreateView.as_view(), name='createblog'),

                       url(r'^user/$', user.IndexView.as_view(), name='users'),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
                       url(r'^user/(?P<pk>\d+)/$', user.DetailView.as_view(), name='userdetail'),

                       # url(r'^skotsj/', include('skotsj.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)
