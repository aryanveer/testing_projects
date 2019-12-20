from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from users.models import Keywords
import json


# class Home(View):
#
# 	def get(self, request):
# 		return render(request, 'dashboard/base.html')

@login_required
def dashboard(request):
	return render(request, 'dashboard/base.html')


@login_required
def channel_monitoring(request):
	group = request.user.groups.values_list('id', flat=True).first()
	keywords = Keywords.objects.filter(group_id=group).values('keyword', 'source', 'priority', 'similar_keywords')
	test_all = json.dumps({"data": list(keywords)})
	data = {'test_data': test_all, }
	return render(request, 'dashboard/keywords.html', data)
