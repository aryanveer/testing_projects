from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .models import Keywords
from django.contrib.auth.decorators import login_required
import json
from django.views import View


class LoginView(View):

	def get(self, request):

		if request.user.is_authenticated:
			return redirect('/dashboard/')

		return render(request, 'users/auth_login.html')

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		ip = request.META['REMOTE_ADDR']
		if ip=='':
			ip = request.META['HTTP_X_REAL_IP']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			if ip in settings.ALLOWED_IP_BLOCKS:
				login(request, user)
				return redirect('/dashboard/')
		else:
			return render(request, 'users/auth_login.html', {'message': "Invalid Username or Password."})


@login_required
def logout_view(request):
	logout(request)
	return redirect('/login/')

