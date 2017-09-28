from django.conf.urls import url
from django.conf.urls.static import static #fixed error typeerrpr
from django.conf import settings

from . import views

urlpatterns = [
    #home page at app1
	url(r'^$', views.ind, name='index'),
    #app1 page
	url(r'^detail/$', views.detail, name='detail'),
	url(r'^showphoto/$', views.photo, name='showphoto'),
	url(r'^new_showphoto/$', views.new_photo, name='new_showphoto'),
    # ex: /app1/5/results/
    #url(r'^(?P<pk>[0-9]+)/results/$', views.results, name='results'),
    # ex: /app1/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)