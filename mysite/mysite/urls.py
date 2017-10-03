from django.conf.urls import include, url
from django.contrib import admin


# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = [
    url(r'^', include('mywebsite.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
