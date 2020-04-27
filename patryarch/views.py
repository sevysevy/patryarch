from django.shortcuts import render
from repertoire.views import dashboard_repertoire


def index(request):
	if request.user.is_authenticated and request.user.myrepertoire.first() :
		return dashboard_repertoire(request, request.user.myrepertoire.first().repertoire_id )
	else:
		return render(request,'patryarch/LANDING_PAGE.html')


