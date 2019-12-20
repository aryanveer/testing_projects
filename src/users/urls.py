from django.urls import path
from . import views

urlpatterns = [
	# path('add/', views.add_keyword),
	path('login/', views.LoginView.as_view()),
	path('logout/', views.logout_view),
	# path('home/', views.index),
]
