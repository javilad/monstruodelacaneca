from django.conf.urls import url
from monstruo import views

urlpatterns = [
    url(r'^recicladores/$', views.RecicladorList.as_view()),
    url(r'^recicladores10/$', views.RecicladorList10.as_view()),
    url(r'^recicladores/(?P<pk>[0-9]+)/$', views.RecicladorDetail.as_view()),
    url(r'^tiporecicladores/$', views.TipoRecicladorList.as_view()),
    url(r'^tiporecicladores/(?P<pk>[0-9]+)/$', views.TipoRecicladorDetail.as_view()),
    url(r'^tipousos/$', views.TipoUsoList.as_view()),
    url(r'^tipousos/(?P<pk>[0-9]+)/$', views.TipoUsoDetail.as_view()),
    url(r'^canecas/$', views.CanecaList.as_view()),
    url(r'^canecas/(?P<pk>[0-9]+)/$', views.CanecaDetail.as_view()),    
    url(r'^residuos/$', views.ResiduoList.as_view()),
    url(r'^residuos/(?P<pk>[0-9]+)/$', views.ResiduoDetail.as_view()),        
    url(r'^partidas/$', views.PartidaList.as_view()),
    url(r'^partidas/(?P<pk>[0-9]+)/$', views.PartidaDetail.as_view()),        
    url(r'^niveles/$', views.NivelList.as_view()),
    url(r'^niveles/(?P<pk>[0-9]+)/$', views.NivelDetail.as_view()),        
]