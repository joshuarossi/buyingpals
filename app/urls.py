# from django.conf.urls.defaults import patterns, include, url
# 
# urlpatterns = patterns('polls.views',
#     url(r'^$', 'index'),
#     url(r'^(?P<poll_id>\d+)/$', 'detail'),
#     url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#     url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
# )

from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from app.models import *

urlpatterns = patterns('app.views',
    url(r'^$', 'home'),
    url(r'^test$', 'test'),
    url(r'^login$', 'login'),
    url(r'^logout$', 'logout'),
    url(r'^signup$', 'signup'),
    url(r'^signin$', 'signin'),
	url(r'^comingsoon$', 'comingsoon'),
	url(r'^post$', 'post'),
	url(r'^confirm$', 'confirm'),
	url(r'^details$', 'details'),

	url(r'^providers$', 'providers'),
	url(r'^search$', 'search'),
	url(r'^searchresults$', 'searchresults'),

	    # project pages
    url(r'^projects$',
        ListView.as_view(
            model=Project,
            # queryset=Poll.objects.order_by('-pub_date')[:5],
            # context_object_name='latest_poll_list',
            template_name='projects/index.html')),
    url(r'^projects/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Project,
            template_name='projects/detail.html')),
    url(r'^projects/(?P<pk>\d+)/created$',
        DetailView.as_view(
            model=Project,
            template_name='projects/created.html')),
    url(r'^vendor$',
        ListView.as_view(
            model=Vendor,
            template_name='vendors/index.html')),

    # vendor pages
    url(r'^vendors/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Vendor,
            template_name='vendors/detail.html')),

    # url(r'^(?P<pk>\d+)/results/$',
    #     DetailView.as_view(
    #         model=Poll,
    #         template_name='polls/results.html'),
    #     name='poll_results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

)
