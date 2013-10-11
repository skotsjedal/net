from django.conf.urls import patterns, include, url
from home import views as home
from blogg import views as blogg
from user import views as user
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.IndexView.as_view(), name='index'),
    url(r'^blogg/$', blogg.IndexView.as_view(), name='blogg'),

    url(r'^user/$', user.IndexView.as_view(), name='users'),
    url(r'^user/(?P<pk>\d+)/$', user.DetailView.as_view(), name='userdetail'),

    # url(r'^skotsj/', include('skotsj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
