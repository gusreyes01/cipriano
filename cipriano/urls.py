from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # Examples:
    # url(r'^$', 'cipriano.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cipriano.views.landing', name='landing'),
    url(r'^home/$', 'cipriano.views.home', name='home'),
    url(r'^contact/$', 'cipriano.views.contact', name='contact'),
    url(r'^studio/$', 'cipriano.views.studio', name='studio'),
    url(r'^team/$', 'cipriano.views.team', name='team'),

]


# Add the static files pattern to the url.
urlpatterns += staticfiles_urlpatterns()
