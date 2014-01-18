from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from recommender import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vestir.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url (r'^api/recommend/$', views.RecommendView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
