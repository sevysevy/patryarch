from django.shortcuts import render


def index(request):
    return render(request,'patryarch/LANDING_PAGE.html')
