from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^about/$',views.about,name='about'),
    url(r'^help/$',views.help,name='help'),
    url(r'^Missions/$',views.Missions,name='Missions'),
    url(r'^Resources/$',views.Resources,name='Resources'),
]