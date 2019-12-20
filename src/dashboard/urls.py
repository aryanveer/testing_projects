from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard),
	path('channel-monitoring', views.channel_monitoring),
]
