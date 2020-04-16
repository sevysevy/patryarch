from django.shortcuts import render
from django.http import  HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy,reverse
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
from .models import *
from .form import *
from .utils import json_tree


def create_repertoire(request):
    if request.method == 'POST':
        form = repertoireform(request.POST)
        if form.is_valid():
            repertoire = form.save()
            return HttpResponseRedirect(reverse('repertoire_dashboard', kwargs={'id':repertoire.id}))
        else:
            form = repertoireform()
            return render(request , 'repertoire/create_repertoire.html',{'form':form})
    else:
        form = repertoireform()
        return render (request , 'repertoire/create_repertoire.html', {'form':form})


def dashboard_repertoire(request, repertoire_id):
    repertoire = Repertoire.objects.get(repertoire_id = repertoire_id)
    request.session["repertoire_id"] = repertoire.repertoire_id
    return render(request,'repertoire/dashboard_repertoire.html',{'repertoire':repertoire})

def repertoire(request, repertoire_id):
    repertoire = Repertoire.objects.get(repertoire_id = repertoire_id)
    request.session["repertoire_id"] = repertoire.repertoire_id
    return render(request, 'repertoire/repertoire.html' , {'repertoire':repertoire})


def tree_views(request):
    repertoire = Repertoire.objects.get(repertoire_id = request.session.get('repertoire_id'))


##############ici on recupere serie,sous serie,division,archives qu'on range dans des tableaux###########
    serie_mere = repertoire.serie_set.all().order_by('cote')
    lis_serie = []

    i_s = 0
    for serie in serie_mere :
        serie_dict = model_to_dict(serie)
        lis_serie.append(serie_dict)

        sousserie_mere = serie.sousserie_set.all().order_by('cote')
        lis_sserie = []

        i_ss = 0
        for sserie in sousserie_mere:
            sserie_dict = model_to_dict(sserie)
            lis_sserie.append(sserie_dict)

            division_mere = sserie.division_set.all().order_by('cote')
            lis_division = []

            i_div = 0
            for division in division_mere:
                division_dict = model_to_dict(division)
                lis_division.append(division_dict)

                archives_mere = division.archives_set.all().order_by('cote')
                lis_archives = []

                i_arch = 0
                for archives in archives_mere:
                    archives_dict = model_to_dict(archives)
                    lis_archives.append(archives_dict)
                    lis_archives[i_arch]["text"] = lis_archives[i_arch].pop("cote") + "  " + lis_archives[i_arch].pop("nom")
                    i_arch += 1

                lis_division[i_div]["nodes"] = lis_archives
                lis_division[i_div]["text"] = lis_division[i_div].pop("cote") + "  " + lis_division[i_div].pop("nom")
                i_div += 1

            lis_sserie[i_ss]["nodes"] = lis_division
            lis_sserie[i_ss]["text"] = lis_sserie[i_ss].pop("cote") + "  " + lis_sserie[i_ss].pop("nom")
            i_ss += 1

        lis_serie[i_s]["nodes"] = lis_sserie
        lis_serie[i_s]["text"] = lis_serie[i_s].pop("cote") + "  " + lis_serie[i_s].pop("nom")
        i_s += 1

    lo = len(lis_serie)
    jo=json_tree(lis_serie)
    
    return JsonResponse (jo , safe= False)



def update_repertoire():
    pass


def delete_repertoire():
    pass

def create_serie(request):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    if request.method == 'POST':
        form = serieform(request.POST)
        if form.is_valid():
            form.instance.repertoire = Repertoire.objects.get(repertoire_id = repertoire_id)
            form.instance.repertoireID = repertoire_id
            serie = form.save()
            data['form_is_valid'] = True
            
        else:
            data['form_is_valid'] = False
    else:
        form = serieform()

    context = {
    'form' : form
    }
    data['html_form'] = render_to_string('repertoire/create_serie.html',context,request=request)
    return JsonResponse(data)
    

def detail_serie(request,cote):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    serie = Repertoire.objects.get(repertoire_id=repertoire_id).serie_set.get(cote=cote)
    context = {
    'serie':serie
    
    }
    data['html'] = render_to_string('repertoire/serie_detail.html', context,request = request)
    return JsonResponse(data)
   

def update_serie(request,cote):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    serie = Repertoire.objects.get(repertoire_id=repertoire_id).serie_set.get(cote=cote)
    if request.method =='POST':
        form = serieform(request.POST, instance=serie)
        if form.is_valid():
            serie = form.save()
        else:
            form = serieform(instance=serie)  
    else:
        form = serieform(instance=serie)
        context = {
        'serie':serie,
        'form':form
        }
        data['html'] = render_to_string('repertoire/serie_update.html', context,request = request)
    return JsonResponse(data)





def delete_serie(request,cote):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    serie = Repertoire.objects.get(repertoire_id=repertoire_id).serie_set.get(cote=cote)
    if request.method == 'POST':
        
        serie.delete()

    context = {
    'serie':serie
    }
    data['html'] = render_to_string('repertoire/serie_delete.html',context,request=request)
    return JsonResponse(data)



def create_sousserie(request):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    if request.method == 'POST':
        form = sousserieform(repertoire_id, request.POST)
        if form.is_valid():
            form.instance.repertoireID = repertoire_id
            sousserie = form.save()
            data['form_is_valid'] = True
            
        else:
            data['form_is_valid'] = False
            
    else:
        form = sousserieform(repertoire_id)
    context = {
    'form' : form
    }
    data['html_form'] = render_to_string('repertoire/create_sousserie.html',context,request=request)
    return JsonResponse(data)


def detail_sousserie(request,cote):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    sserie = SousSerie.objects.get(cote=cote,repertoireID=repertoire_id)
    context = {
    'sousserie':sserie
    
    }
    data['html'] = render_to_string('repertoire/sousserie_detail.html', context,request = request)
    return JsonResponse(data)


def update_sousserie():
    pass

def delete_sousserie():
    pass



def create_division(request):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    if request.method == 'POST':
        form = divisionform(repertoire_id ,request.POST)
        if form.is_valid():
            form.instance.repertoireID = repertoire_id
            division = form.save()
            data['form_is_valid'] = True
            
        else:
            data['form_is_valid'] = False
    else:
        form = divisionform(repertoire_id)
    context = {
    'form' : form
    }
    data['html_form'] = render_to_string('repertoire/create_division.html',context,request=request)
    return JsonResponse(data)


def detail_division(request,cote):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    division = Division.objects.get(cote=cote,repertoireID=repertoire_id)
    context = {
    'division':division
    
    }
    data['html'] = render_to_string('repertoire/division_detail.html', context,request = request)
    return JsonResponse(data)

def update_division():
    pass

def delete_division():
    pass



def create_archives(request):
    repertoire_id = request.session.get('repertoire_id')

    data = dict()
    if request.method == 'POST':
        form = archivesform(repertoire_id, request.POST)
        if form.is_valid():
            form.instance.repertoireID = repertoire_id
            archives = form.save()
            data['form_is_valid'] = True

        else:
            data['form_is_valid'] = False
            
    else:
        form = archivesform(repertoire_id)
    context = {
    'form' : form
    }
    data['html_form'] = render_to_string('repertoire/create_archives.html',context,request=request)
    return JsonResponse(data)

        
def detail_archive(request,cote):
    repertoire_id = request.session.get('repertoire_id')
    data = dict()
    archive = Archives.objects.get(cote=cote,repertoireID=repertoire_id)
    context = {
    'archive':archive
    
    }
    data['html'] = render_to_string('repertoire/archive_detail.html', context,request = request)
    return JsonResponse(data)

def update_archives():
    pass

def delete_archives():
    pass



def create_boitearchive(request, repertoire_id):
    if request.method == 'POST':
        form = boitearchiveform(request.POST)
        if form.is_valid():
            form.instance.repertoire = Repertoire.objects.get(repertoire_id = repertoire_id)
            boitearchive = form.save()
            return HttpResponseRedirect(reverse('repertoire_archives', kwargs={'repertoire_id':repertoire_id}))
        else:
            form = boitearchiveform()
            return render(request , 'repertoire/create_boitearchive.html', {'form':form})
    else:
        form = boitearchiveform()
        return render(request , 'repertoire/create_boitearchive.html', {'form':form})

def update_boitearchive():
    pass

def delete_boitearchive():
    pass
