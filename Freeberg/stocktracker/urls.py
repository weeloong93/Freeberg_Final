from django.conf.urls import url
from . import views

app_name = 'stocktracker'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^allstocks/$', views.allstocks, name='allstocks'),
    url(r'^pickstock1/$', views.pickstock1, name='pickstock1'),
    url(r'^(?P<stock_id>[0-9]+)/$', views.individual_stock, name='individual_stock'),
    url(r'^(?P<stock_id1>[0-9]+)/pickstock2/$', views.pickstock2, name='pickstock2'),
    url(r'^(?P<stock_id1>[0-9]+)/(?P<stock_id2>[0-9]+)/$', views.comparison, name='comparison'),

]
