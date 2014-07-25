from django.conf.urls import patterns, include, url
from tweet_sentiment_analysis.views import *

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_p.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^tweet_list/(\d*)/$', tweet_list, name="list"),
    url(r'^tweet_details/(\d*)/$', tweet_details, name="details"),
)
