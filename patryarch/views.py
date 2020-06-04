from django.shortcuts import render
from repertoire.views import dashboard_repertoire,create_repertoire
from django.http import  HttpResponseRedirect
from django.urls import reverse_lazy,reverse


def index(request):
	if request.user.is_authenticated:
		if request.user.myrepertoire.first() :
			repertoire = request.user.myrepertoire.first()
			return HttpResponseRedirect(reverse('repertoire_dashboard',kwargs={'repertoire_id' : repertoire.repertoire_id}))
		else :
			return create_repertoire(request)

	else:
		return render(request,'patryarch/LANDING_PAGE.html')


