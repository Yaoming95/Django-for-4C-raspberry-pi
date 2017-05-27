from django.conf.urls import patterns, include, url
from django.contrib import admin
from  news import views as news_view
from control import views as control_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raspberry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', news_view.index, name = 'home' ),
    url(r'^control', control_view.index, ),
    url(r'^add/$', control_view.add, name='add'),

)
