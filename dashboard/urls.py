from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home_view, (), 'home'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.category_view, name='category'),

    url(r'^category_visualizations/(?P<slug>[\w-]+)/$',
        views.category_visualization_view,
        name='embedded_viz_list'),

    url(r'^visualization/(?P<slug>[\w-]+)/$',
        views.visualization_view,
        name='embedded_viz'),

    url(r'^authorize/$', views.socrata_authorize_view, name='authorize'),
    url(r'^callback/$', views.socrata_callback_view, name='callback'),
]
