from django.conf.urls import url
from django.conf.urls.static import static #fixed error typeerrpr
from django.conf import settings

from . import views

urlpatterns = [
    #app2 page
	url(r'^testupload/$', views.testupload, name='testupload'),
	url(r'^newindex/$', views.newindex, name='newindex'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)